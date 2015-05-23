#!/usr/bin/env python
# encoding: utf-8
import ast


class SugarReplacer(ast.NodeTransformer):
    BINOP_TRANSLATION = {
            ast.Add: 'add',
            ast.Sub: 'sub',
            ast.Mult: 'mul',
            ast.Div: 'truediv',
            ast.Mod: 'mod',
            ast.Pow: 'pow',
            ast.LShift: 'lshift',
            ast.RShift: 'rshift',
            ast.BitOr: 'or',
            ast.BitXor: 'xor',
            ast.BitAnd: 'and',
            ast.FloorDiv: 'floordiv'
    }
    UNARYOP_TRANSLATION = {
            ast.Invert: 'invert',
            ast.UAdd: 'pos',
            ast.USub: 'neg'
    }
    COMPARE_TRANSLATION = {
            ast.Eq: 'eq',
            ast.NotEq: 'ne',
            ast.Lt: 'lt',
            ast.LtE: 'le',
            ast.Gt: 'gt',
            ast.GtE: 'ge',
    }

    class Not(ast.AST):
        _fields = ('value',)

        def __init__(self, value):
            self.value = value

    # TODO
    # x.__len__() <==> len(x)
    # x.__delitem__(y) <==> del x[y]
    # x.__delslice__(i, j) <==> del x[i:j]
    # x.__contains__(y) <==> y in x
    # x.__iadd__(y) <==> x+=y
    # x.__imul__(y) <==> x*=y
    # Etc

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        try:
            op_name = '__%s__' % self.BINOP_TRANSLATION[type(node.op)]
        except KeyError:
            raise NotYetSupported('binary operation', node.op)
        op = ast.Attribute(value=left, attr=op_name, ctx=ast.Load())
        return ast.Call(func=op, args=[right], keywords=[], starargs=None,
                        kwargs=None)

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)

        if isinstance(node.op, ast.Not):
            return BuiltinReplacer.Not(operand)
        else:
            try:
                op_name = '__%s__' % self.UNARYOP_TRANSLATION[type(node.op)]
            except KeyError:
                raise NotYetSupported('unary operation', node.op)
            op = ast.Attribute(value=operand, attr=op_name, ctx=ast.Load())
            return ast.Call(func=op, args=[], keywords=[], starargs=None,
                            kwargs=None)

    def visit_Compare(self, node):
        left = self.visit(node.left)
        comparison_nodes = []
        for op, comparator in zip(node.ops, node.comparators):
            comparator = self.visit(comparator)
            try:
                op_name = '__%s__' % self.COMPARE_TRANSLATION[type(op)]
            except KeyError:
                raise NotYetSupported('comparison operator', op)
            op = ast.Attribute(value=left, attr=op_name, ctx=ast.Load())
            comparison = ast.Call(func=op, args=[comparator], keywords=[],
                                  starargs=None, kwargs=None)
            comparison_nodes.append(comparison)
            left = comparator

        return ast.BoolOp(op=ast.And(), values=comparison_nodes)

    # def visit_Subscript(self, node):
    #     self.visit(node.value)
    #     self.visit(node.slice)
    #     if isinstance(node.slice, ast.Index):
    #         if isinstance(node.ctx, ast.Load):
    #             op_name = '__getitem__'
    #         elif isinstance(node.ctx, ast.Store):
    #             op_name = '__setitem__'
    #         elif isinstance(node.ctx, ast.Del):
    #             op_name = '__delitem__'
    #     elif isinstance(node.slice, ast.Slice):
    #         if isinstance(node.ctx, ast.Load):
    #             op_name = '__getslice__'
    #         elif isinstance(node.ctx, ast.Store):
    #             op_name = '__setslice__'
    #         elif isinstance(node.ctx, ast.Del):
    #             op_name = '__delslice__'
    #     # TODO verander node
    #     return node


def replace_syntactic_sugar(module):
    replacer = SugarReplacer()
    replacer.visit(module)
