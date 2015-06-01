from logging import debug

from typy.exceptions import NoSuchAttribute, CantSetBuiltinAttribute
from typy.types import Type
from typy.builtin.functions import BuiltinFunction as Fun


class BuiltinDataType(Type):
    def __init__(self):
        self.attributes = {}

    def check(self):
        debug('checking type', repr(self))
        return self

    def get_attribute(self, name):
        try:
            return self.attributes[name]
        except KeyError:
            raise NoSuchAttribute(self, name)

    def set_attribute(self, name, value):
        raise CantSetBuiltinAttribute(self)

    def __repr__(self):
        return self.__class__.__name__


class BuiltinObject(BuiltinDataType):
    def __init__(self):
        super().__init__()
        self.attributes.update({
            # '__class__': x,
        })


class Int(BuiltinObject):
    def __init__(self):
        super().__init__()
        self.attributes.update({
            '__add__': Fun('__add__', [Int], Int),
            '__invert__': Fun('__invert__', [], Int),
            '__lt__': Fun('__lt__', [Int], Bool),
        })


class Bool(Int):
    def __init__(self):
        super().__init__()
        self.attributes.update({
            '__abs__': Fun('__abs__', [Bool], Int),
            '__add__': Fun('__add__', [Bool], Int),
            '__and__': Fun('__and__', [Bool], Int),
            '__bool__': Fun('__bool__', [Bool], Int),
            '__ceil__': Fun('__ceil__', [Bool], Int),
            '__divmod__': Fun('__divmod__', [Bool], Int),
            '__float__': Fun('__float__', [Bool], Int),
            '__floor__': Fun('__floor__', [Bool], Int),
            '__floordiv__': Fun('__floordiv__', [Bool], Int),
            '__getnewargs__': Fun('__getnewargs__', [Bool], Int),
            '__index__': Fun('__index__', [Bool], Int),
            '__int__': Fun('__int__', [Bool], Int),
            '__invert__': Fun('__invert__', [Bool], Int),
            '__lshift__': Fun('__lshift__', [Bool], Int),
            '__mod__': Fun('__mod__', [Bool], Int),
            '__mul__': Fun('__mul__', [Bool], Int),
            '__neg__': Fun('__neg__', [Bool], Int),
            '__or__': Fun('__or__', [Bool], Int),
            '__pos__': Fun('__pos__', [Bool], Int),
            '__pow__': Fun('__pow__', [Bool], Int),
            '__radd__': Fun('__radd__', [Bool], Int),
            '__rand__': Fun('__rand__', [Bool], Int),
            '__rdivmod__': Fun('__rdivmod__', [Bool], Int),
            '__rfloordiv__': Fun('__rfloordiv__', [Bool], Int),
            '__rlshift__': Fun('__rlshift__', [Bool], Int),
            '__rmod__': Fun('__rmod__', [Bool], Int),
            '__rmul__': Fun('__rmul__', [Bool], Int),
            '__ror__': Fun('__ror__', [Bool], Int),
            '__round__': Fun('__round__', [Bool], Int),
            '__rpow__': Fun('__rpow__', [Bool], Int),
            '__rrshift__': Fun('__rrshift__', [Bool], Int),
            '__rshift__': Fun('__rshift__', [Bool], Int),
            '__rsub__': Fun('__rsub__', [Bool], Int),
            '__rtruediv__': Fun('__rtruediv__', [Bool], Int),
            '__rxor__': Fun('__rxor__', [Bool], Int),
            '__sub__': Fun('__sub__', [Bool], Int),
            '__truediv__': Fun('__truediv__', [Bool], Int),
            '__trunc__': Fun('__trunc__', [Bool], Int),
            '__xor__': Fun('__xor__', [Bool], Int),
            'bit_length': Fun('bit_length', [Bool], Int),
            'conjugate': Fun('conjugate', [Bool], Int),
            'denominator': Fun('denominator', [Bool], Int),
            'from_bytes': Fun('from_bytes', [Bool], Int),
            'imag': Fun('imag', [Bool], Int),
            'numerator': Fun('numerator', [Bool], Int),
            'real': Fun('real', [Bool], Int),
            'to_bytes': Fun('to_bytes', [Bool], Int),
        })


class Float(BuiltinDataType):
    pass


class Complex(BuiltinDataType):
    pass


class Str(BuiltinDataType):
    pass


class None_(BuiltinDataType):
    pass


class Any(BuiltinDataType):  # Not really builtin type, but behaves like it
    def get_attribute(self, name):
        return self

    @staticmethod
    def istypeof(object_):
        return True


def add_to_type_map(type_map):
    TYPES = [
        ('bool', Bool),
        # ('bytearray', Bytearray),
        # ('bytes', Bytes),
        # ('classmethod', Classmethod),
        # ('complex', Complex),
        # ('dict', Dict),
        # ('enumerate', Enumerate),
        # ('filter', Filter),
        # ('float', Float),
        # ('frozenset', Frozenset),
        ('int', Int),
        # ('list', List),
        # ('map', Map),
        # ('memoryview', Memoryview),
        # ('object', Object),
        # ('property', Property),
        # ('range', Range),
        # ('reversed', Reversed),
        # ('set', Set),
        # ('slice', Slice),
        # ('staticmethod', Staticmethod),
        # ('str', Str),
        # ('super', Super),
        # ('tuple', Tuple),
        # ('type', Type),
        # ('zip', Zip),
    ]

    for name, type_ in TYPES:
        type_map.add_variable(name, type_())


# TODO not implemented:
# BuiltinFunctionType
# BuiltinMethodType
# CodeType
# DynamicClassAttribute
# FrameType
# FunctionType
# GeneratorType
# GetSetDescriptorType
# LambdaType
# MappingProxyType
# MemberDescriptorType
# MethodType
# ModuleType {'__loader__', '__name__', '__package__', '__spec__'},
# SimpleNamespace
# TracebackType
# NoneType
# NotImplementedType
# ellipsis (=type(Ellipsis)à
# ClassType
# InstanceType
# FileType
