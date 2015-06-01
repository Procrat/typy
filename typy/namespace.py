from collections import UserDict
from logging import debug

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
        # self.stack = []
        self.current_namespace = global_namespace

    def find(self, name):
        # debug('stack =', self.stack)
        debug('ns =', self.current_namespace)
        # if len(self.stack) > 0 and name in self.stack[-1]:
            # debug(name, 'found in local namespace')
            # return self.stack[-1][name]
        # else:
        for super_namespace in self.current_namespace.iter_super_namespaces():
            if name in super_namespace:
                debug(name, 'found in', super_namespace.fqn(), 'namespace')
                return super_namespace[name]
        raise NoSuchName(name, self.current_namespace)

    def build_context_for(self, name):
        context = Namespace(name + '.<locals>', self.current_namespace)
        # if len(self.stack) > 0:
            # context.update(self.stack[-1])
        return context

    def enter_namespace(self, name):
        self.current_namespace = Namespace(name, self.current_namespace)
        return self.current_namespace

    def exit_namespace(self):
        self.current_namespace = self.current_namespace.parent

    def enter_function_scope(self, context, initial_mapping=None):
        function_namespace = context.copy()
        if initial_mapping is not None:
            function_namespace.update(initial_mapping)
        self.current_namespace = function_namespace
        # self.stack.append(function_namespace)

    def exit_function_scope(self):
        self.current_namespace = self.current_namespace.parent
        # self.stack.pop()

    def add_variable(self, name, object_):
        # TODO check if name exist and is of other type
        # If so, create intersection type
        self.current_namespace[name] = object_

    # def copy_namespace(self, class_namespace, object_):
        # new_objects = {}

        # for name, value in self.heap.items():
            # if class_namespace in name:
                # new_fqn = name.replace(class_namespace, object_.namespace)
                # if isinstance(value, FunctionDef):
                    # value = Method(self, object_, value, object_.namespace)
                # new_objects[new_fqn] = value

        # self.heap.update(new_objects)


# class NodeVisitor:
    # def visit(self, node):
        # method = 'visit_' + node.__class__.__name__
        # visitor = getattr(self, method, self.generic_visit)
        # return visitor(node)

    # def generic_visit(self, node):
        # for child in node.iter_child_nodes():
            # self.visit(child)


# class NamespaceBuilder(NodeVisitor):
    # def __init__(self, global_namespace):
        # self.global_namespace = global_namespace

    # def generic_visit(self, node):
        # self._set_namespace_on_children(node, node.namespace)
        # super().generic_visit(node)

    # def visit_Module(self, node):
        # children_namespace = Namespace('__main__', self.global_namespace)
        # self._set_namespace_on_children(node, node.namespace)
        # super().generic_visit(node)

    # def visit_ClassDef(self, node):
        # children_namespace = Namespace(node.name, node.namespace)
        # self._set_namespace_on_children(node, children_namespace)
        # super().generic_visit(node)

    # def visit_FunctionDef(self, node):
        # children_namespace = Namespace(node.name, node.namespace)
        # self._set_namespace_on_children(node, children_namespace)
        # super().generic_visit(node)

    # def _set_namespace_on_children(self, node, namespace):
        # for child in node.iter_child_nodes():
            # child.namespace = namespace


# def build_namespaces(module):
    # global_namespace = Namespace('__builtin__', None)
    # namespace_builder = NamespaceBuilder(global_namespace)
    # namespace_builder.visit(module)


def build_type_map():
    global_namespace = Namespace('global', None)
    return TypeMap(global_namespace)
