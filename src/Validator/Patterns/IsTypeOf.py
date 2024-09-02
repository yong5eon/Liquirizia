# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from collections.abc import Iterable
from typing import Sequence

__all__ = (
	'IsTypeOf',
	'IsBool',
	'IsInteger',
	'IsFloat',
	'IsString',
	'IsList',
	'IsTuple',
	'IsDictionary',
	'IsBytes',
	'IsByteStream',
)


class IsTypeOf(Pattern):
	def __init__(
		self, 
		type     : type,
		patterns : Sequence[Pattern] = (),
		error                        = None
	):
		self.type = type
		self.patterns = patterns if isinstance(patterns, Iterable) else (patterns,)
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, self.type):
			if self.error:
				raise self.error
			raise TypeError('{} must be {}'.format(parameter, self.type.__name__))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.type.__name__,
		)


class IsBool(IsTypeOf):
	def __init__(self, *args, error=None):
		super(IsBool, self).__init__(bool, patterns=args, error=error)
		return

class IsInteger(IsTypeOf):
	def __init__(self, *args, error=None):
		super(IsInteger, self).__init__(int, patterns=args, error=error)
		return


class IsFloat(IsTypeOf):
	def __init__(self, *args, error=None):
		super(IsFloat, self).__init__(float, patterns=args, error=error)
		return


class IsString(IsTypeOf):
	def __init__(self, *args, error=None):
		super(IsString, self).__init__(str, patterns=args, error=error)
		return


class IsList(IsTypeOf):
	def __init__(self, *args, error=None):
		super(IsList, self).__init__(list, patterns=args, error=error)
		return


class IsTuple(IsTypeOf):
	def __init__(self, *args, error=None):
		super(IsTuple, self).__init__(tuple, patterns=args, error=error)
		return


class IsDictionary(IsTypeOf):
	def __init__(self, *args, error=None):
		super(IsDictionary, self).__init__(dict, patterns=args, error=error)
		return

class IsBytes(IsTypeOf):
	def __init__(self, *args, error=None):
		super(IsBytes, self).__init__(bytes, patterns=args, error=error)
		return

class IsByteStream(IsTypeOf):
	def __init__(self, *args, error=None):
		super(IsByteStream, self).__init__(bytearray, patterns=args, error=error)
		return
