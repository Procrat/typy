import ast
from logging import debug

from typy.builtin import data_types
from typy.exceptions import NotYetSupported, NoSuchAttribute, NotIterable
from typy.types import Type, Function, Class


class Node:
    def __init__(self, type_map, ast_node):
        self.type_map = type_map
        self._ast_fields = ast_node._fields

    def check(self):
        """Must be overriden in subtype."""
        raise NotYetSupported('check call to', self)

    def iter_fields(self):
        for field in self._ast_fields:
            try:
                yield field, getattr(self, field)
            except AttributeError:
                pass

    def iter_child_nodes(self):
        for _name, field in self.iter_fields():
            if isinstance(field, Node):
                yield field
            elif isinstance(field, list):
                for item in field:
                    if isinstance(item, Node):
                        yield item


class FunctionDef(Node):
    def __init__(self, type_map, ast_node):
        if (ast_node.args.vararg is not None or
                len(ast_node.args.kwonlyargs) > 0 or
                len(ast_node.args.kw_defaults) > 0 or
                ast_node.args.kwarg is not None or
                len(ast_node.args.defaults) > 0):
            raise NotYetSupported('default arguments and keyword arguments')

        super().__init__(type_map, ast_node)
        self.name = ast_node.name
        self.params = [arg.arg for arg in ast_node.args.args]
        self.body = [convert(type_map, stmt) for stmt in ast_node.body]
        self._ast_fields = ('name', 'params', 'body')

    def check(self):
        debug('checking func def %s', self.name)
        function = Function(self, self.type_map)
        self.type_map.add_variable(self.name, function)

    def __repr__(self):
        return 'def ' + self.name + '()'


class ClassDef(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.name = ast_node.name
        self.body = [convert(type_map, stmt) for stmt in ast_node.body]

    def check(self):
        debug('checking class def %s', self.name)

        class_namespace = self.type_map.enter_namespace(self.name)

        for stmt in self.body:
            stmt.check()

        self.type_map.exit_namespace()

        class_ = Class(self, self.type_map, class_namespace)
        self.type_map.add_variable(self.name, class_)

    def __repr__(self):
        return 'def ' + self.name


class Attribute(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.value = convert(type_map, ast_node.value)
        self.attr = ast_node.attr
        self.ctx = ast_node.ctx

    def check(self):
        debug('checking attr %s', self)

        value_type = self.value.check()
        debug('attr %r = %r', self, value_type)

        if isinstance(self.ctx, ast.Load):
            return value_type.get_attribute(self.attr)
        elif isinstance(self.ctx, ast.Store):
            return (value_type, self.attr)
        else:
            # TODO implement for Del, AugLoad, AugStore, Param
            raise NotYetSupported('name context', self.ctx)

    def __repr__(self):
        return repr(self.value) + '.' + self.attr


class Name(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.id = ast_node.id
        self.ctx = ast_node.ctx

    def check(self):
        debug('checking name %s', self.id)

        if isinstance(self.ctx, ast.Load):
            return self.type_map.find(self.id)
        elif isinstance(self.ctx, ast.Store):
            return self
        else:
            # TODO implement for Del, AugLoad, AugStore, Param
            raise NotYetSupported('name context', self.ctx)

    def __repr__(self):
        return self.id


class Call(Node):
    def __init__(self, type_map, ast_node):
        if (len(ast_node.keywords) > 0 or
                ast_node.starargs is not None or
                ast_node.kwargs is not None):
            raise NotYetSupported('keyword arguments and star arguments')

        super().__init__(type_map, ast_node)
        self.func = convert(type_map, ast_node.func)
        self.args = [convert(type_map, expr) for expr in ast_node.args]

    def check(self):
        debug('checking call')
        func = self.func.check()
        args = [arg.check() for arg in self.args]
        return func.check_call(args)

    def __repr__(self):
        return repr(self.func) + \
               '(' + ', '.join(repr(x) for x in self.args) + ')'


class Expr(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.value = convert(type_map, ast_node.value)

    def check(self):
        debug('checking expr')
        return self.value.check()

    def __repr__(self):
        return repr(self.value)


class Return(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.value = convert(type_map, ast_node.value)

    def check(self):
        debug('checking return')
        return self.value.check()

    def __repr__(self):
        return 'return ' + repr(self.value)


class Module(Node, Type):
    def __init__(self, type_map, ast_node):
        Node.__init__(self, type_map, ast_node)
        Type.__init__(self, type_map)
        self.body = [convert(type_map, stmt) for stmt in ast_node.body]

    def check(self):
        debug('checking module')

        self.module_namespace = self.type_map.enter_namespace('__main__')

        debug('entering %r', self.type_map.current_namespace)

        for stmt in self.body:
            debug('still in %r', self.type_map.current_namespace)
            stmt.check()

        debug('leaving %r', self.type_map.current_namespace)

        self.type_map.exit_namespace()

    def get_attribute(self, name):
        try:
            return self.module_namespace[name]
        except KeyError:
            Type.get_attribute(self, name)


class Assign(Node):
    def __init__(self, type_map, ast_node):
        # TODO handle multiple targets
        if len(ast_node.targets) > 1:
            raise NotYetSupported('assignment with multiple targets')

        super().__init__(type_map, ast_node)
        self.target = convert(type_map, ast_node.targets[0])
        self.value = convert(type_map, ast_node.value)
        self._ast_fields = ('target', 'value')

    def check(self):
        debug('checking assign %r', self.target)

        _assign(self.target, self.value, self.type_map)

    def __repr__(self):
        return repr(self.target) + ' = ' + repr(self.value)


class Pass(Node):
    def check(self):
        debug('checking pass')

    def __repr__(self):
        return 'pass'


class Not(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.value = convert(type_map, ast_node.value)

    def check(self):
        debug('checking not')
        self.value.check()
        return data_types.Bool()

    def __repr__(self):
        return 'not ' + repr(self.value)


class BoolOp(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.op = ast_node.op
        self.values = [convert(type_map, value) for value in ast_node.values]

    def check(self):
        debug('checking boolop')

        for value in self.values:
            value.check()
        # TODO return intersection van types?

    def __repr__(self):
        op_name = ' {} '.format(self.op)
        return '(' + op_name.join(repr(val) for val in self.values) + ')'


class In(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.element = convert(type_map, ast_node.element)
        self.container = convert(type_map, ast_node.container)

    def check(self):
        debug('checking in')

        element = self.element.check()
        container = self.container.check()

        try:
            container.call_magic_method('__contains__', element)
        except NoSuchAttribute:
            if not container.is_iterable():
                raise NotIterable(container)

        return data_types.Bool()

    def __repr__(self):
        return '{!r} in {!r}'.format(self.element, self.container)


class For(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.target = convert(type_map, ast_node.target)
        self.iter = convert(type_map, ast_node.iter)
        self.body = [convert(type_map, stmt) for stmt in ast_node.body]
        self.orelse = [convert(type_map, clause) for clause in ast_node.orelse]

    def check(self):
        debug('checking for')

        iterator = self.iter.check()
        enclosed_type = iterator.get_enclosed_type()
        _assign(self.target, enclosed_type, self.type_map)

        for stmt in self.body:
            stmt.check()
        for stmt in self.orelse:
            stmt.check()

    def __repr__(self):
        s = 'for {!r} in {!r}:\n    '.format(self.target, self.iter)
        s += '\n    '.join(repr(stmt) for stmt in self.body)
        if self.orelse:
            s += 'else:\n    '
            s += '\n    '.join(repr(stmt) for stmt in self.orelse)
        return s


class If(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.test = convert(type_map, ast_node.test)
        self.body = [convert(type_map, stmt) for stmt in ast_node.body]
        self.orelse = [convert(type_map, stmt) for stmt in ast_node.orelse]

    def check(self):
        debug('checking if')

        # TODO take isinstance into account (?)
        # TODO real branching?
        self.test.check()
        for stmt in self.body:
            stmt.check()
        for stmt in self.orelse:
            stmt.check()

    def __repr__(self):
        s = 'if {!r}:\n    '.format(self.test)
        s += '\n    '.join(repr(stmt) for stmt in self.body)
        if self.orelse:
            s += 'else:\n    '
            s += '\n    '.join(repr(stmt) for stmt in self.orelse)
        return s


class IfExp(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.test = convert(type_map, ast_node.test)
        self.body = convert(type_map, ast_node.body)
        self.orelse = convert(type_map, ast_node.orelse)

    def check(self):
        debug('checking ifexp')

        # TODO take isinstance into account (?)
        # TODO real branching?
        self.test.check()
        self.body.check()
        self.orelse.check()

    def __repr__(self):
        template = '{!r} if {!r} else {!r}'
        return template.format(self.test, self.body, self.orelse)


class NameConstant(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.value = ast_node.value

    def check(self):
        debug('checking name constant %r', self.value)
        if self.value is None:
            return data_types.None_()
        elif self.value is True or self.value is False:
            return data_types.Bool()
        else:
            raise NotYetSupported('name constant', self.value)

    def __repr__(self):
        return repr(self.value)


class While(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.test = convert(type_map, ast_node.test)
        self.body = [convert(type_map, stmt) for stmt in ast_node.body]
        self.orelse = [convert(type_map, stmt) for stmt in ast_node.orelse]

    def check(self):
        debug('checking while')

        # TODO take isinstance into account (?)
        # TODO real branching?
        self.test.check()
        for stmt in self.body:
            stmt.check()
        for stmt in self.orelse:
            stmt.check()

    def __repr__(self):
        s = 'while {!r}:\n    '.format(self.test)
        s += '\n    '.join(repr(stmt) for stmt in self.body)
        if self.orelse:
            s += 'else:\n    '
            s += '\n    '.join(repr(stmt) for stmt in self.orelse)
        return s


class Break(Node):
    def check(self):
        debug('checking break')

    def __repr__(self):
        return 'break'


class Continue(Node):
    def check(self):
        debug('checking continue')

    def __repr__(self):
        return 'continue'


class Num(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.number_type = {
            int: data_types.Int,
            # float: data_types.Float,
            # complex: data_types.Complex,
        }[type(ast_node.n)]

    def check(self):
        debug('checking num')
        return self.number_type()


class Tuple(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.elts = [convert(type_map, el) for el in ast_node.elts]
        self.ctx = ast_node.ctx

    def check(self):
        debug('checking tuple %r', self)

        if isinstance(self.ctx, ast.Load):
            el_types = (el.check() for el in self.elts)
            return data_types.Tuple(self.type_map, *el_types)
        elif isinstance(self.ctx, ast.Store):
            return self
        else:
            # TODO implement for Del, AugLoad, AugStore, Param
            raise NotYetSupported('name context', self.ctx)

    def __repr__(self):
        return '(' + ', '.join(repr(el) for el in self.elts) + ')'


def _assign(target, value, type_map):
    value_type = value.check()

    if isinstance(target, Name):
        target_type = target.check()
        type_map.add_variable(target_type.id, value_type)
    elif isinstance(target, Attribute):
        target_type, attr = target.check()
        target_type.set_attribute(attr, value_type)
    else:
        raise NotYetSupported('assignment to', target)


def convert(type_map, node):
    class_name = node.__class__.__name__
    try:
        # Try to convert to a node
        class_ = globals()[class_name]
        return class_(type_map, node)
    except KeyError:
        try:
            # Try to convert to a builtin type
            class_ = getattr(data_types, class_name)
            return class_()
        except AttributeError:
            raise NotYetSupported('node', node)
