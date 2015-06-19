class NotYetSupported(Exception):
    def __init__(self, kind, thing=None):
        self.msg = 'Support for {}'.format(kind)
        if thing is not None:
            self.msg += ' "{}"'.format(type(thing).__name__)
        self.msg += ' is not yet implemented'


class CheckError(Exception):
    pass


class NoSuchName(CheckError):
    def __init__(self, name, namespace):
        template = '{} not found in namespace {}'
        self.msg = template.format(name, namespace.fqn())


class NoSuchAttribute(CheckError):
    def __init__(self, type_, attribute):
        template = '{} has no attribute {}'
        self.msg = template.format(type_, attribute)


class WrongBuiltinArgument(CheckError):
    def __init__(self, name, param, arg):
        template = 'Builtin function {} expected {} but got {}.'
        self.msg = template.format(name, param, arg)


class WrongArgumentsLength(CheckError):
    def __init__(self, name, params_length, args_length):
        template = '{} expected {} parameters, but received {}'
        self.msg = template.format(name, params_length, args_length)


class NotCallable(CheckError):
    def __init__(self, value):
        template = '{} is not callable'
        self.msg = template.format(value)


class InvalidAssignmentTarget(CheckError):
    def __init__(self, target):
        template = "can't assign to {}"
        self.msg = template.format(target)


class NotIterable(CheckError):
    def __init__(self, non_iterable):
        template = 'object {} is not iterable'
        self.msg = template.format(non_iterable)


class CantSetBuiltinAttribute(CheckError):
    def __init__(self, builtin_type):
        template = "can't set attributes of built-in/extension type {}"
        self.msg = template.format(builtin_type)
