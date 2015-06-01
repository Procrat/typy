import ast

from typy.exceptions import NotYetSupported


# TODO
# x.__len__() <==> len(x)
# x.__delitem__(y) <==> del x[y]
# x.__delslice__(i, j) <==> del x[i:j]
# x.__contains__(y) <==> y in x
# x.__iadd__(y) <==> x+=y
# x.__imul__(y) <==> x*=y
# Etc


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


class In(ast.AST):
    _fields = ('element', 'container')


class SugarReplacer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        try:
            op_name = '__%s__' % BINOP_TRANSLATION[type(node.op)]
        except KeyError:
            raise NotYetSupported('binary operation', node.op)
        return _make_method_call(left, op_name, [right])

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)

        if isinstance(node.op, ast.Not):
            return Not(operand)
        else:
            try:
                op_name = '__%s__' % UNARYOP_TRANSLATION[type(node.op)]
            except KeyError:
                raise NotYetSupported('unary operation', node.op)
            return _make_method_call(operand, op_name, [])

    def visit_Compare(self, node):
        left = self.visit(node.left)
        comparison_nodes = []
        for op, comparator in zip(node.ops, node.comparators):
            comparator = self.visit(comparator)
            comparison = _make_comparison(left, op, comparator)
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


def _make_method_call(caller, method, args):
    method = ast.Attribute(value=caller, attr=method, ctx=ast.Load())
    return ast.Call(func=method, args=args, keywords=[], starargs=None,
                    kwargs=None)


def _make_comparison(left, op, right):
    if isinstance(op, ast.In):
        return In(left, right)
    elif isinstance(op, ast.NotIn):
        return Not(In(left, right))
    else:
        try:
            op_name = '__%s__' % COMPARE_TRANSLATION[type(op)]
        except KeyError:
            raise NotYetSupported('comparison operator', op)
        return _make_method_call(left, op_name, [right])


def replace_syntactic_sugar(module):
    replacer = SugarReplacer()
    replacer.visit(module)
