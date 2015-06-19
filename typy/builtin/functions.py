#!/usr/bin/env python
# encoding: utf-8
from logging import debug

from typy.types import Type, Class
from typy.exceptions import WrongBuiltinArgument


class BuiltinFunction(Type):
    def __init__(self, name, param_type_clss, return_type):
        self.name = name
        self.param_type_clss = param_type_clss
        self.return_type = return_type

    def check_call(self, args):
        debug('call check %s %s', self.name, args)

        for param_type, arg in zip(self.param_type_clss, args):
            if not param_type.istypeof(arg):
                raise WrongBuiltinArgument(self.name, param_type, arg)

        return self.return_type()

    def __repr__(self):
        return self.name + '()'


def add_to_type_map(type_map):
    from typy.builtin.data_types import Any, Str, Int, Bool, None_

    FUNCTIONS = [
        # 'abs' should be converted to __abs__
        # ('all', [Iterable(Any)], Bool),
        # ('any', [Iterable(Any)], Bool),
        ('ascii', [Any], Str),
        ('bin', [Int], Str),
        ('callable', [Any], Bool),
        ('chr', [Int], Str),
        # 'compile': types.CodeType,
        # 'delattr' should be converted to __delattr__
        # ('dir', [Optional(Any)], Iterable(Str)),
        # ('divmod', [Num, Num], Tuple((Num, Num))),
        # ('eval', [Str, Optional(Dict(Str, Any)), Optional(Dict(Str, Any))],
        #  Any),
        # ('exec', [Intersection(Str, Code), Optional(Dict(Str, Any)),
        #           Optional(Dict(Str, Any))], None_),
        # ('format', [Any, Optional(Str)], Str),
        # 'getattr' should be converted to __getattribute__
        # ('globals', [], Dict(Str, Any)),
        # ('hasattr', [Any, Str], Bool),
        # 'hash' should be converted to __hash__
        ('hex', [Int], Str),
        ('id', [Any], Int),
        ('input', [], Str),
        # TODO actually with prompt: ('input', [Optional(Str)], Str),
        ('isinstance', [Any, Class], Bool),
        ('issubclass', [Class, Class], Bool),
        # 'iter' should be converted to __iter__ or handled specially
        #    no support for iter-with-sentinel?
        # 'len' Should have been converted to __len__
        # ('locals', [], Dict(Str, Any)),
        # 'max' TODO multiple ways to call
        # 'min' TODO multiple ways to call
        # 'next' TODO should be handled in a special way
        ('oct', [Int], Str),
        # ('open', [Str, ...], FileObject),  # TODO
        ('ord', [Str], Int),
        # ('pow', [Num, Num, Optional(Num)], Num),
        ('print', [Any], None_),  # TODO handle multiple arguments
        ('repr', [Any], Str),
        # ('round', [Num, Optional(Num)], Num),
        # 'setattr' should be converted to __setattr__
        # 'sorted' TODO should be handled in a special way
        # 'sum' TODO convert Iterable(x) to x
        # ('vars', [Optional(Any)], Dict(Str, Any)),
    ]
    # Typy doesn't support the builtin printing functions:
    #   copyright(), credit(), help(), license()

    for function_name, arg_types, return_type in FUNCTIONS:
        function = BuiltinFunction(function_name, arg_types, return_type)
        type_map.add_variable(function_name, function)
