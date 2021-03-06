"""
This module handles namespaces. The TypeMap keeps track of the current
namespace during each step of the type checking process as it browses through
the code.
"""

from collections import UserDict
from logging import debug, warn

from typy.exceptions import NoSuchName


class Namespace(UserDict):
    """A namespace is a mapping of names to types"""

    def __init__(self, name, parent):
        super().__init__()
        self.name = name
        self.parent = parent

    def __repr__(self):
        return '{}({!r},{!r})'.format(self.name, self.data, self.parent)

    def fqn(self):
        if self.parent is None or self.parent.fqn() == 'global':
            return self.name
        else:
            return self.parent.fqn() + '.' + self.name

    def iter_super_namespaces(self):
        namespace = self
        while namespace is not None:
            yield namespace
            namespace = namespace.parent


class TypeMap:
    def __init__(self, global_namespace):
        self.stack = []
        self.current_namespace = global_namespace

    def find(self, name):
        debug('ns = %s', self.current_namespace)
        for super_namespace in self.current_namespace.iter_super_namespaces():
            if name in super_namespace:
                debug('%s found in %s namespace', name, super_namespace.fqn())
                return super_namespace[name]
        raise NoSuchName(name, self.current_namespace)

    def build_context_for(self, name):
        return Namespace(name + '.<locals>', self.current_namespace)

    def enter_namespace(self, name):
        self.current_namespace = Namespace(name, self.current_namespace)
        return self.current_namespace

    def exit_namespace(self):
        self.current_namespace = self.current_namespace.parent

    def enter_function_scope(self, context, initial_mapping=None):
        self.stack.append(self.current_namespace)

        function_namespace = context.copy()
        if initial_mapping is not None:
            function_namespace.update(initial_mapping)
        self.current_namespace = function_namespace

    def exit_function_scope(self):
        self.current_namespace = self.stack.pop()

    def add_variable(self, name, object_):
        if (name in self.current_namespace and
                not self.current_namespace[name].istypeof(object_)):
            warn('Overriding name with different type: %r instead of %r',
                 object_, self.current_namespace[name])

        self.current_namespace[name] = object_


def build_type_map():
    global_namespace = Namespace('global', None)
    return TypeMap(global_namespace)
