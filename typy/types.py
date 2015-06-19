"""
This module contains all logic on how builtin Python objects behave.

In short, this defines how they handle attributes, lexical scoping,
instantiation and how they handle being called.
"""

from logging import debug

from typy.exceptions import NoSuchAttribute, NotCallable, NotYetSupported, \
    WrongArgumentsLength


class Type:
    def __init__(self, type_map, attributes=None):
        self.type_map = type_map
        self.attributes = attributes or {}

    def get_attribute(self, name):
        try:
            return self.attributes[name]
        except KeyError:
            raise NoSuchAttribute(self, name)
            # TODO check existence of getattribute method

    def set_attribute(self, name, value):
        # TODO check existence of setattribute method
        self.attributes[name] = value

    def check_call(self, args):
        # TODO check for existence of __call__ and call check_call on it
        raise NotCallable(self)

    def istypeof(self, object_):
        if self.__class__ == object_.__class__:
            return True

        raise NotYetSupported('istypeof call to', self)


class Function(Type):
    def __init__(self, func_def, type_map):
        super().__init__(type_map)
        self.name = func_def.name
        self.params = func_def.params
        self.body = func_def.body
        self.context = type_map.build_context_for(self.name)

    def check_call(self, args):
        debug('call check %s', self.name)

        if len(self.params) != len(args):
            raise WrongArgumentsLength(self.name, len(self.params), len(args))

        param_map = {param: arg for param, arg in zip(self.params, args)}
        debug('  %r', param_map)
        self.type_map.enter_function_scope(self.context, param_map)

        for stmt in self.body:
            return_type = stmt.check()

        self.type_map.exit_function_scope()

        return return_type

    def __repr__(self):
        return self.name + '()'


class Class(Type):
    def __init__(self, class_def, type_map, class_namespace):
        super().__init__(type_map, class_namespace)
        self.name = class_def.name
        self.body = class_def.body

    def check_call(self, args):
        try:
            new_func = self.get_attribute('__new__')
            instance = new_func.check_call(args)
        except NoSuchAttribute:
            instance = Instance(self, self.type_map)

        try:
            # TODO explicit __new__ call
            instance.call_magic_method('__init__', args)
        except NoSuchAttribute:
            # TODO check supertype inits
            pass

        return instance

    def get_attribute(self, name):
        return super().get_attribute(name)

        # TODO search var/meth in supertypes
        # TODO search in std class vars/meths

    def __repr__(self):
        return self.name


class Instance(Type):
    def __init__(self, class_, type_map=None):
        super().__init__(type_map)
        self.class_ = class_

    def call_magic_method(self, name, args):
        magic_function = self.class_.get_attribute(name)
        magic_method = Method(self.type_map, self, magic_function)
        return magic_method.check_call(args)

    def get_attribute(self, name):
        try:
            return super().get_attribute(name)
        except NoSuchAttribute:
            class_attr = self.class_.get_attribute(name)
            if isinstance(class_attr, Function):
                return Method(self.type_map, self, class_attr)
            else:
                return class_attr

    def istypeof(self, object_):
        if not isinstance(object_, Instance):
            return False
        return self.class_.istypeof(object_.class_)

    def check(self):
        return self

    def __repr__(self):
        return repr(self.class_) + '()'

    def __str__(self):
        return '{} object'.format(self.class_)


class Method(Type):
    """A method is represented as a wrapper around a function within a class"""

    def __init__(self, type_map, object_, function):
        super().__init__(type_map)
        self.object_ = object_
        self.function = function

    def __getattr__(self, name):
        return getattr(self.function, name)

    def check_call(self, args):
        debug('method call check %s.%s', self.object_, self.function)
        return self.function.check_call([self.object_] + args)

    def __repr__(self):
        return repr(self.object_) + '.' + self.name + '()'


class Tuple(Type):
    def __init__(self, type_map, *elements):
        super().__init__(type_map)
        self.elements = elements

    def __repr__(self):
        return '(' + ', '.join(repr(el) for el in self.elements) + ')'


class Intersection(Type):
    def __init__(self, type_map, *types):
        super().__init__(type_map)
        self.types = types

    def call_magic_method(self, name, args):
        return_types = [type_.call_magic_method(name, args)
                        for type_ in self.types]
        return Intersection(return_types)

    def check_call(self, args):
        return_types = [type_.check_call(args) for type_ in self.types]
        return Intersection(return_types)

    def get_attribute(self, name):
        attribute_types = [type_.get_attribute(name) for type_ in self.types]
        return Intersection(attribute_types)

    def istypeof(self, object_):
        return all(type_.istypeof(object_) for type_ in self.types)

    def __call__(self, *args, **kwargs):
        return self

    def __repr__(self):
        return '(' + ' | '.join(repr(t) for t in self.types) + ')'
