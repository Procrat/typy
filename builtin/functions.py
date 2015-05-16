#!/usr/bin/env python
# encoding: utf-8

import types
from test import BuiltinFunctionType, Num


FUNCTIONS = {
    # 'abs' should be converted to __abs__
    'all': bool,
    'any': bool,
    'ascii': str,
    'bin': str,
    'bool': bool,
    'bytearray': bytearray,
    'bytes': bytes,
    'callable': bool,
    'chr': str,
    'classmethod': classmethod,
    'compile': types.CodeType,
    'complex': complex,
    'copyright': type(None),
    'credits': type(None),
    # 'delattr' should be converted to __delattr__
    'dict': dict,
    'dir': list,
    'divmod': tuple,
    'enumerate': enumerate,
    'eval': object,
    'exec': type(None),
    'filter': filter,
    'float': float,
    'format': str,
    'frozenset': frozenset,
    # 'getattr' should be converted to __getattribute__
    'globals': dict,
    'hasattr': bool,
    # 'hash' should be converted to __hash__
    'help': type(None),
    'hex': str,
    'id': int,
    'input': str,
    'int': int,
    'isinstance': bool,
    'issubclass': bool,
    # 'iter' should be converted to __iter__
    # 'len' Should have been converted to __len__
    'license': type(None),
    'list': list,
    'locals': dict,
    'map': map,
    # 'max' TODO
    'memoryview': memoryview, # TODO verwacht bytes/bytearray
    # 'min' TODO
    # 'next' should be converted to __next__
    'object': object,
    'oct': str,
    # 'open' find a solution
    'ord': int,
    # 'pow': num TODO
    'print': type(None),
    # 'property' TODO
    'range': range,
    'repr': repr,
    # 'reversed' TODO iter/next
    'round': int,
    'set': set,
    # 'setattr' should be converted to __setattr__
    'slice': slice,
    'sorted': list,
    'staticmethod': staticmethod,
    'str': str,
    # 'sum' TODO
    # 'super' TODO
    'tuple': tuple,
    'type': type,
    'vars': dict,
    'zip': zip
}
