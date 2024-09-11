# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from decimal import Decimal

from collections.abc import Iterable, Sequence, Mapping
from typing import Type, Tuple

__all__ = (
	'IsTypeOf',
	'IsBool',
	'IsInteger',
	'IsFloat',
	'IsString',
	'IsList',
	'IsTuple',
	'IsDictionary',
	'IsByteArray',
	'IsByteStream',
	'IsDecimal',
	'ToTypeOf',
	'ToBool',
	'ToInteger',
	'ToFloat',
	'ToString',
	'ToList',
	'ToTuple',
	'ToDictionary',
	'ToByteArray',
	'ToByteStream',
	'ToDecimal',
)


class IsTypeOf(Pattern):
	def __init__(
		self, 
		type     : Type,
		patterns : Tuple[Pattern] = (),
		error                     = None
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
		super().__init__(bool, patterns=args, error=error)
		return

class IsInteger(IsTypeOf):
	def __init__(self, *args, error=None):
		super().__init__(int, patterns=args, error=error)
		return


class IsFloat(IsTypeOf):
	def __init__(self, *args, error=None):
		super().__init__(float, patterns=args, error=error)
		return


class IsString(IsTypeOf):
	def __init__(self, *args, error=None):
		super().__init__(str, patterns=args, error=error)
		return


class IsList(IsTypeOf):
	def __init__(self, *args, error=None):
		super().__init__(Sequence, patterns=args, error=error)
		return


class IsTuple(IsTypeOf):
	def __init__(self, *args, error=None):
		super().__init__(Sequence, patterns=args, error=error)
		return


class IsDictionary(IsTypeOf):
	def __init__(self, *args, error=None):
		super().__init__(Mapping, patterns=args, error=error)
		return


class IsByteArray(IsTypeOf):
	def __init__(self, *args, error=None):
		super().__init__(bytes, patterns=args, error=error)
		return


class IsByteStream(IsTypeOf):
	def __init__(self, *args, error=None):
		super().__init__(bytearray, patterns=args, error=error)
		return
	

class IsDecimal(IsTypeOf):
	def __init__(self, *args, error=None):
		super().__init__(Decimal, patterns=args, error=error)
		return


class ToTypeOf(Pattern):
	def __init__(self, type : type, error=None):
		self.type = type
		self.error = error
		return

	def __call__(self, parameter):
		try:
			return self.type(parameter)
		except Exception as e:
			if self.error:
				raise self.error
			raise e

	def __repr__(self):
		return '{}()'.format(self.type.__name__)
	


class ToBool(ToTypeOf):
	def __init__(self, error=None):
		super().__init__(bool, error)
		return


class ToInteger(ToTypeOf):
	def __init__(self, error=None):
		super().__init__(int, error)
		return


class ToFloat(ToTypeOf):
	def __init__(self, error=None):
		super().__init__(float, error)
		return


class ToString(ToTypeOf):
	def __init__(self, error=None):
		super().__init__(str, error)
		return


class ToList(ToTypeOf):
	def __init__(self, error=None):
		super().__init__(list, error)
		return


class ToTuple(ToTypeOf):
	def __init__(self, error=None):
		super().__init__(tuple, error)
		return


class ToDictionary(ToTypeOf):
	def __init__(self, error=None):
		super().__init__(dict, error)
		return
	

class ToByteArray(ToTypeOf):
	def __init__(self, error=None):
		super().__init__(bytes, error)
		return


class ToByteStream(ToTypeOf):
	def __init__(self, error=None):
		super().__init__(bytearray, error)
		return


class ToDecimal(ToTypeOf):
	def __init__(self, error=None):
		super().__init__(Decimal, error)
		return