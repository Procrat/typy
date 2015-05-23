#!/usr/bin/env python
# encoding: utf-8
"""
Glossary
--------
 - `fqn` stand for `fully qualified name`, which is a stringification of the
   occurence of an object in the namespace hierarchy.
"""

import ast
import builtin.types
import insuline
from exceptions import (NoSuchName, NoSuchAttribute, WrongBuiltinArgument,
                        WrongArgumentsLength, CheckError, NotYetSupported)


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
        for name, field in self.iter_fields():
            if isinstance(field, Node):
                yield field
            elif isinstance(field, list):
                for item in field:
                    if isinstance(item, Node):
                        yield item


class Type(Node):
    def get_attribute(self, name):
        # TODO make this decent, i.e. without an ugly call to a map
        return builtin.types.ATTRIBUTE_MAP[self.__class__.__name__][name]
        # """Must be overriden in subtype."""
        # raise NotYetSupported('has_attribute of', self)

    def check_call(self, args):
        # TODO check for existence of __call__ and call check_call on it
        raise NotYetSupported('check_call call to', self)

    @classmethod
    def istypeof(cls, object_):
        if isinstance(object_, cls):
            return True

        # TODO check if args has all attributes of type
        raise NotYetSupported('istypeof call to', cls())


class Module(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.body = [convert(type_map, stmt) for stmt in ast_node.body]

    def check(self):
        print('checking module')
        for stmt in self.body:
            stmt.check()


class FunctionDef(Type):
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
        print('checking fdef', self.name)
        fqn = self.namespace + '.' + self.name
        self.type_map.stateful_push(fqn, self)

    def check_call(self, args):
        print('call check', self.name)

        if len(self.params) != len(args):
            raise WrongArgumentsLength(self.name, len(self.params), len(args))

        function_scope = {param: arg for param, arg in zip(self.params, args)}
        print('  ', function_scope)
        self.type_map.push(function_scope)

        for stmt in self.body:
            return_type = stmt.check()

        self.type_map.pop()

        return return_type

    def __repr__(self):
        return self.name + '(...)'


class Return(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.value = convert(type_map, ast_node.value)

    def check(self):
        print('checking return')
        return self.value.check()

    def __repr__(self):
        return 'return ' + repr(self.value)


class Expr(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.value = convert(type_map, ast_node.value)

    def check(self):
        print('checking expr')
        return self.value.check()

    def __repr__(self):
        return repr(self.value)


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
        print('checking call')
        func = self.func.check()
        args = [arg.check() for arg in self.args]
        return func.check_call(args)

    def __repr__(self):
        return repr(self.func) + \
               '(' + ', '.join(repr(x) for x in self.args) + ')'


class Name(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.id = ast_node.id
        self.ctx = ast_node.ctx

    def check(self):
        print('checking name', self.id)
        if isinstance(self.ctx, ast.Load):
            return self.type_map.find(self.id, self.namespace)
        elif isinstance(self.ctx, ast.Store):
            pass
        else:
            # TODO implement for Del
            raise NotYetSupported('name context', self.ctx)

    def __repr__(self):
        return self.id


class Attribute(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.value = convert(type_map, ast_node.value)
        self.attr = ast_node.attr

    def check(self):
        print('checking attr', self)

        value_type = self.value.check()
        print('attr', self, '=', value_type)

        return value_type.get_attribute(self.attr)

    def __repr__(self):
        return repr(self.value) + '.' + self.attr


class Method(Type):
    """A method is represented as a wrapper around a function within a class"""

    def __init__(self, type_map, object_, function, namespace):
        self.type_map = type_map
        self.object_ = object_
        self.function = function
        self.namespace = namespace

    def __getattr__(self, name):
        return getattr(self.function, name)

    def check_call(self, args):
        print('method call check')
        return self.function.check_call([self.object_] + args)

    def __repr__(self):
        return repr(self.object_) + '.' + self.name + '(...)'


class ClassDef(Type):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        self.name = ast_node.name
        self.body = [convert(type_map, stmt) for stmt in ast_node.body]

    def check(self):
        print('checking class def', self.name)

        for stmt in self.body:
            stmt.check()

        fqn = self.namespace + '.' + self.name
        self.type_map.stateful_push(fqn, self)

    def check_call(self, args):

        # TODO refactor this
        class Instance(Type):
            class_ = self

            def __init__(self):
                print('HIERZO', self.__class__.__qualname__)
                self.type_map = self.class_.type_map
                self.namespace = self.class_.namespace + '.' + \
                    self.class_.name + '_' + hex(id(self))[2:]
                self.type_map.copy_namespace(self.class_._class_namespace(),
                                             self)

            def get_attribute(self, name):
                try:
                    attr = self.type_map.find(name, self.namespace)
                    print('gevonden', attr)
                    return attr
                except NoSuchName:
                    raise NoSuchAttribute(self, name, self.namespace)
                # TODO Zoek var/meth in supertypes
                # TODO Zoek in std class vars/meths

            def __repr__(self):
                return repr(self.class_) + '(...)'

        instance = Instance()

        try:
            init_meth = self.type_map.find('__init__', self._class_namespace())
            init_meth.check_call([instance] + args)
        except NoSuchName:
            # TODO check supertype inits
            pass

        return instance

    def get_attribute(self, name):
        try:
            return self.type_map.find(name, self._class_namespace())
        except NoSuchName:
            raise NoSuchAttribute(self, name, self.namespace)

        # TODO Zoek var/meth in supertypes
        # TODO Zoek in std class vars/meths

    def _class_namespace(self):
        return self.namespace + '.' + self.name

    def __repr__(self):
        return self.name


class Assign(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)
        # TODO handle multiple targets
        self.target = convert(type_map, ast_node.targets[0])
        self.value = convert(type_map, ast_node.value)
        self._ast_fields = ('target', 'value')

    def check(self):
        print('checking assign', self.target)
        value_type = self.value.check()
        target_type = self.target.check()
        # TODO Handle attributes seperately
        # TODO add to heap? temporarely? depending on local or not?

    def __repr__(self):
        return repr(self.target) + ' = ' + repr(self.value)


class Pass(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)

    def check(self):
        print('checking pass')


class Not(Node):
    def __init__(self, type_map, ast_node):
        super().__init__(type_map, ast_node)

    def check(self):
        return builtin.types.Bool()


class BuiltinFunction(Type):
    def __init__(self, name, param_type_clss, return_type):
        self._ast_fields = ()
        self.namespace = '__builtins__'
        self.name = name
        self.param_type_clss = param_type_clss
        self.return_type = return_type

    def check(self):
        print('checking builtin fct def', self.name)

    def check_call(self, args):
        print('CALL CHECK', self.name, args)

        for param_type, arg in zip(self.param_type_clss, args):
            if not param_type.istypeof(arg):
                raise WrongBuiltinArgument(self.name, param_type, arg)

        return self.return_type

    def __repr__(self):
        return self.name


class NodeVisitor:
    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for child in node.iter_child_nodes():
            self.visit(child)


class NamespaceBuilder(NodeVisitor):
    def generic_visit(self, node):
        self._set_namespace_on_children(node, node.namespace)
        super().generic_visit(node)

    def visit_Module(self, node):
        node.namespace = '__main__'
        self._set_namespace_on_children(node, node.namespace)
        super().generic_visit(node)

    def visit_ClassDef(self, node):
        children_namespace = node.namespace + '.' + node.name
        self._set_namespace_on_children(node, children_namespace)
        super().generic_visit(node)

    def visit_FunctionDef(self, node):
        children_namespace = node.namespace + '.' + node.name
        self._set_namespace_on_children(node, children_namespace)
        super().generic_visit(node)

    def _set_namespace_on_children(self, node, namespace):
        for child in node.iter_child_nodes():
            child.namespace = namespace


class TypeMap:
    def __init__(self):
        self.heap = {}
        self.stack = []

    def find(self, name, namespace):
        if len(self.stack) > 0 and name in self.stack[-1]:
            return self.stack[-1][name]
        else:
            for super_namespace in iter_super_namespaces(namespace):
                fqn = super_namespace + '.' + name
                if fqn in self.heap:
                    return self.heap[fqn]
        raise NoSuchName(name, namespace)

    def push(self, type_map):
        self.stack.append(type_map)

    def pop(self):
        return self.stack.pop()

    def stateful_push(self, fqn, type_):
        self.heap[fqn] = type_

    def copy_namespace(self, class_namespace, object_):
        new_objects = {}

        for name, value in self.heap.items():
            if class_namespace in name:
                new_fqn = name.replace(class_namespace, object_.namespace)
                if isinstance(value, FunctionDef):
                    value = Method(self, object_, value, object_.namespace)
                new_objects[new_fqn] = value

        self.heap.update(new_objects)


def convert(type_map, node):
    class_name = node.__class__.__name__
    try:
        # Try to convert to a node
        class_ = globals()[class_name]
        return class_(type_map, node)
    except KeyError:
        try:
            # Try to convert to a builtin type
            class_ = getattr(builtin.types, class_name)
            return class_()
        except AttributeError:
            raise NotYetSupported('node', node)


def iter_super_namespaces(namespace):
    while '.' in namespace:
        yield namespace
        namespace = namespace[:namespace.rindex('.')]
    yield namespace
    yield '__builtins__'


def main(file_):
    module = ast.parse(open(file_).read())

    print(ast.dump(module))

    try:
        insuline.replace_syntactic_sugar(module)

        print(ast.dump(module))

        type_map = TypeMap()

        module = convert(type_map, module)

        namespace_builder = NamespaceBuilder()
        namespace_builder.visit(module)

        # TODO make a decent system to handle builtin functions
        Num = builtin.types.Num
        Any = builtin.types.Any
        print_func = BuiltinFunction('print', [Any], Num())
        type_map.stateful_push('__builtins__.print', print_func)

        try:
            module.check()
            print('All checks passed!')
        except CheckError as error:
            print('Failed:', error.msg)

    except NotYetSupported as error:
        print(error.msg)


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
