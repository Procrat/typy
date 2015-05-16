#!/usr/bin/env python
# encoding: utf-8


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
        self.msg = template.format(name, namespace)


class NoSuchAttribute(CheckError):
    def __init__(self, value, attribute, namespace):
        template = '{} has no attribute {} (in {})'
        self.msg = template.format(value, attribute, namespace)


class WrongBuiltinArgument(CheckError):
    def __init__(self, name, param, arg):
        template = 'Builtin function {} expected {} but got {}.'
        self.msg = template.format(name, param, arg)


class WrongArgumentsLength(CheckError):
    def __init__(self, name, params_length, args_length):
        template = '{} expected {} parameters, but received {}'
        self.msg = template.format(name, params_length, args_length)
