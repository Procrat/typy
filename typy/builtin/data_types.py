from logging import debug

from typy.exceptions import NoSuchAttribute, CantSetBuiltinAttribute
from typy.types import Type, Instance
from typy.builtin.functions import BuiltinFunction as Fun


class BuiltinDataInstance(Instance):
    def set_attribute(self, name, value):
        raise CantSetBuiltinAttribute(self)


class Int(BuiltinDataInstance):
    def __init__(self):
        super().__init__(IntType())


class Bool(BuiltinDataInstance):
    def __init__(self):
        super().__init__(BoolType())


class Str(BuiltinDataInstance):
    def __init__(self):
        super().__init__(StrType())


class None_(BuiltinDataInstance):
    def __init__(self):
        super().__init__(NoneType())


class BuiltinDataType(Type):
    def __init__(self):
        self.attributes = {
            # '__class__': Type(),
            # '__delattr__',
            # '__dir__': Fun('__dir__', [], List(Str)),
            '__doc__': Str,
            '__eq__': Fun('__eq__', [Any], Bool),
            '__format__': Fun('__format__', [Str], Str),
            '__ge__': Fun('__ge__', [Any], Bool),
            # '__getattribute__',
            '__gt__': Fun('__gt__', [Any], Bool),
            '__hash__': Fun('__hash__', [], Int),
            # '__init__': Fun('__init__', [...], ...),
            '__le__': Fun('__le__', [Any], Bool),
            '__lt__': Fun('__lt__', [Any], Bool),
            '__ne__': Fun('__ne__', [Any], Bool),
            # '__new__',
            '__reduce__': Fun('__reduce__', [], Str),
            '__reduce_ex__': Fun('__reduce_ex__', [Int], Str),
            '__repr__': Fun('__repr__', [], Str),
            # '__setattr__',
            '__sizeof__': Fun('__sizeof__', [], Int),
            '__str__': Fun('__str__', [], Str),
            '__subclasshook__': Fun('__subclasshook__', [Any], Bool),
        }

    def check(self):
        debug('checking type %r', self)
        return self

    def istypeof(self, object_):
        if isinstance(object_, self.__class__):
            return True

    def get_attribute(self, name):
        try:
            return self.attributes[name]
        except KeyError:
            raise NoSuchAttribute(self, name)

    def set_attribute(self, name, value):
        raise CantSetBuiltinAttribute(self)

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return 'object'


class IntType(BuiltinDataType):
    def __init__(self):
        super().__init__()
        self.attributes.update({
            '__abs__': Fun('__abs__', [], Int),
            '__add__': Fun('__add__', [Int], Int),
            '__and__': Fun('__and__', [Any], Int),
            '__bool__': Fun('__bool__', [], Bool),
            '__ceil__': Fun('__ceil__', [], Int),
            # '__divmod__': Fun('__divmod__', [Int], Tuple(Int, Int)),
            # '__float__': Fun('__float__', [], Float),
            '__floor__': Fun('__floor__', [], Int),
            '__floordiv__': Fun('__floordiv__', [Int], Int),
            # '__getnewargs__': Fun('__getnewargs__', [Int], Int),
            '__index__': Fun('__index__', [], Int),
            '__int__': Fun('__int__', [], Int),
            '__invert__': Fun('__invert__', [], Int),
            '__lshift__': Fun('__lshift__', [Int], Int),
            '__mod__': Fun('__mod__', [Int], Int),
            '__mul__': Fun('__mul__', [Int], Int),
            '__neg__': Fun('__neg__', [], Int),
            '__or__': Fun('__or__', [Any], Int),
            '__pos__': Fun('__pos__', [], Int),
            # '__pow__': Fun('__pow__', [Int, Optional(Int)], Int),
            '__radd__': Fun('__radd__', [Int], Int),
            '__rand__': Fun('__rand__', [Any], Int),
            # '__rdivmod__': Fun('__rdivmod__', [Int], Tuple(Int, Int)),
            '__rfloordiv__': Fun('__rfloordiv__', [Int], Int),
            '__rlshift__': Fun('__rlshift__', [Int], Int),
            '__rmod__': Fun('__rmod__', [Int], Int),
            '__rmul__': Fun('__rmul__', [Int], Int),
            '__ror__': Fun('__ror__', [Any], Int),
            '__round__': Fun('__round__', [], Int),
            '__rpow__': Fun('__rpow__', [Int], Int),
            '__rrshift__': Fun('__rrshift__', [Int], Int),
            '__rshift__': Fun('__rshift__', [Int], Int),
            '__rsub__': Fun('__rsub__', [Int], Int),
            '__rtruediv__': Fun('__rtruediv__', [Int], Int),
            '__rxor__': Fun('__rxor__', [Any], Int),
            '__sub__': Fun('__sub__', [Int], Int),
            '__truediv__': Fun('__truediv__', [Int], Int),
            '__trunc__': Fun('__trunc__', [], Int),
            '__xor__': Fun('__xor__', [Any], Int),
            'bit_length': Fun('bit_length', [], Int),
            # 'conjugate': Fun('conjugate', [], Complex),
            'denominator': Int,
            # 'from_bytes': Fun('from_bytes', [Bytes], Int),
            'imag': Int,
            'numerator': Int,
            'real': Int,
            # 'to_bytes': Fun('to_bytes', [Int, Str], Bytes),
        })

    def check_call(self, args):
        # TODO Check args = (Optional(Intersect(Num, string, bytes, of has __int__)), Optional(Integer))
        return self

    def __str__(self):
        return 'int'


class BoolType(IntType):
    def __str__(self):
        return 'bool'


class StrType(BuiltinDataType):
    def __init__(self):
        super().__init__()
        # TODO
        # self.attributes.update({
        #     '__add__',
        #     '__contains__',
        #     '__getitem__',
        #     '__getnewargs__',
        #     '__iter__',
        #     '__len__',
        #     '__mod__',
        #     '__mul__',
        #     '__rmod__',
        #     '__rmul__',
        #     'capitalize',
        #     'casefold',
        #     'center',
        #     'count',
        #     'encode',
        #     'endswith',
        #     'expandtabs',
        #     'find',
        #     'format',
        #     'format_map',
        #     'index',
        #     'isalnum',
        #     'isalpha',
        #     'isdecimal',
        #     'isdigit',
        #     'isidentifier',
        #     'islower',
        #     'isnumeric',
        #     'isprintable',
        #     'isspace',
        #     'istitle',
        #     'isupper',
        #     'join',
        #     'ljust',
        #     'lower',
        #     'lstrip',
        #     'maketrans',
        #     'partition',
        #     'replace',
        #     'rfind',
        #     'rindex',
        #     'rjust',
        #     'rpartition',
        #     'rsplit',
        #     'rstrip',
        #     'split',
        #     'splitlines',
        #     'startswith',
        #     'strip',
        #     'swapcase',
        #     'title',
        #     'translate',
        #     'upper',
        #     'zfill'
        # }

    def __str__(self):
        return 'str'


class NoneType(BuiltinDataType):
    def __init__(self):
        super().__init__()
        self.attributes.update({
            '__bool__': Fun('__bool__', [], Bool),
        })

    def __str__(self):
        return 'None'


class Any(BuiltinDataType):  # Not really builtin type, but behaves like it
    def get_attribute(self, name):
        return self

    @staticmethod
    def istypeof(object_):
        return True

    def __str__(self):
        return '<any>'


def add_to_type_map(type_map):
    TYPES = [
        ('bool', BoolType),
        # ('bytearray', Bytearray),
        # ('bytes', Bytes),
        # ('classmethod', Classmethod),
        # ('complex', Complex),
        # ('dict', Dict),
        # ('enumerate', Enumerate),
        # ('filter', Filter),
        # ('float', Float),
        # ('frozenset', Frozenset),
        ('int', IntType),
        # ('list', List),
        # ('map', Map),
        # ('memoryview', Memoryview),
        ('object', BuiltinDataType),
        # ('property', Property),
        # ('range', Range),
        # ('reversed', Reversed),
        # ('set', Set),
        # ('slice', Slice),
        # ('staticmethod', Staticmethod),
        ('str', StrType),
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
