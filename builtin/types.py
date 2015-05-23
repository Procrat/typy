#!/usr/bin/env python
# encoding: utf-8

import types
from typy import Type, BuiltinFunction


class BuiltinDataType(Type):
    def __init__(self):
        pass

    def check(self):
        print('checking type', self.__class__)
        return self


class Num(BuiltinDataType):
    def __repr__(self):
        return 'num'


class Bool(BuiltinDataType):
    def __repr__(self):
        return 'bool'


class Any(BuiltinDataType):  # Not really builtin type, but behaves like it
    def get_attribute(self, name):
        return self

    @staticmethod
    def istypeof(object_):
        return True

    def __repr__(self):
        return 'any'


# Unsupported magic methods:



ATTRIBUTE_MAP = {
    'Num': {
        '__add__': BuiltinFunction('__add__', [Num], Num()),
        '__invert__': BuiltinFunction('__invert__', [], Num()),
        '__lt__': BuiltinFunction('__lt__', [Num], Bool()),
    },

    'None': set(dir(None)),
    'object': set(dir(object)),
    'function': set(dir(types.FunctionType)),

    object: set(dir(object)),
    NotImplemented: set(dir(NotImplemented)),
    Ellipsis: set(dir(Ellipsis)),
    slice: set(dir(slice)),
    types.BuiltinFunctionType: set(dir(types.BuiltinFunctionType)),
    types.FunctionType: set(dir(types.FunctionType)),
    types.MethodType: set(dir(types.MethodType)),
    types.GeneratorType: set(dir(types.GeneratorType)),

    types.ModuleType: set(dir(object)) | {
        '__builtins__',
        '__cached__',
        '__file__',
        '__loader__',
        '__name__',
        '__package__',
        '__spec__'},

    # classmethod, enumerate, filter, map, staticmethod
    # zip
    # NoneType = type(None)
    # TypeType = type
    # ObjectType = object
    # IntType = int
    # LongType = long
    # FloatType = float
    # BooleanType = bool
    # StringType = str
    # TupleType = tuple
    # ListType = list
    # DictType = DictionaryType = dict
    # set, frozenset
    # str, bytes, bytearray
    # range
    # complex
    # bytes, bytearray

    # class _C:
        # def _m(self): pass
    # ClassType = type(_C)
    # UnboundMethodType = type(_C._m)         # Same as MethodType
    # _x = _C()
    # InstanceType = type(_x)

    # FileType = file
    # range

    # types.MemberDescriptorType
    # types.CodeType
    # types.GetSetDescriptorType
    # types.DynamicClassAttribute
    # types.LambdaType
    # types.SimpleNamespace
    # types.FrameType
    # types.MappingProxyType
    # types.TracebackType
}
# for type_ in ATTRIBUTE_MAP:
    # ATTRIBUTE_MAP[type_] |= set(dir(object))

#
# num supports:
#   ['__abs__',
#    '__add__',
#    '__and__',
#    '__bool__',
#    '__ceil__',
#    '__divmod__',
#    '__float__',
#    '__floor__',
#    '__floordiv__',
#    '__getnewargs__',
#    '__index__',
#    '__int__',
#    '__invert__',
#    '__lshift__',
#    '__mod__',
#    '__mul__',
#    '__neg__',
#    '__or__',
#    '__pos__',
#    '__pow__',
#    '__radd__',
#    '__rand__',
#    '__rdivmod__',
#    '__rfloordiv__',
#    '__rlshift__',
#    '__rmod__',
#    '__rmul__',
#    '__ror__',
#    '__round__',
#    '__rpow__',
#    '__rrshift__',
#    '__rshift__',
#    '__rsub__',
#    '__rtruediv__',
#    '__rxor__',
#    '__sub__',
#    '__truediv__',
#    '__trunc__',
#    '__xor__',
#    'bit_length',
#    'conjugate',
#    'denominator',
#    'from_bytes',
#    'imag',
#    'numerator',
#    'real',
#    'to_bytes']
