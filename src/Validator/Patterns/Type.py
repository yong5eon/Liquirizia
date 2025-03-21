# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from decimal import Decimal
from dataclasses import is_dataclass
from collections.abc import (
	Iterable,
	MutableSequence,
	Sequence,
	MutableSet,
	Set,
	MutableMapping,
	Mapping,
)

from typing import Type, Sequence as TSequence

__all__ = (
	'IsTypeOf',
	'IsBool',
	'IsInteger',
	'IsFloat',
	'IsString',
	'IsArray',
	'IsList',
	'IsTuple',
	'IsSet',
	'IsFixedSet',
	'IsDictionary',
	'IsFixedDictionary',
	'IsByteArray',
	'IsByteStream',
	'IsDecimal',
	'IsDataObject',
	'ToTypeOf',
	'ToBool',
	'ToInteger',
	'ToFloat',
	'ToString',
	'ToList',
	'ToTuple',
	'ToSet',
	'ToDictionary',
	'ToByteArray',
	'ToByteStream',
	'ToDecimal',
)


class IsTypeOf(Pattern):
	def __init__(
		self, 
		type: Type,
		patterns: TSequence[Pattern] = (),
		error: BaseException = None
	):
		self.type = type
		self.patterns = patterns if isinstance(patterns, Iterable) else (patterns,)
		self.error = error
		return

	def __call__(self, parameter):
		op = {
			MutableSequence: lambda o: not isinstance(o, self.type),
			Sequence: lambda o: not isinstance(o, self.type),
			MutableSet: lambda o: not isinstance(o, self.type),
			Set: lambda o: not isinstance(o, self.type),
			MutableMapping: lambda o: not isinstance(o, self.type),
			Mapping: lambda o: not isinstance(o, self.type),
		}.get(self.type, lambda o: not type(parameter) is self.type)
		if op(parameter):
			if self.error:
				raise self.error
			raise TypeError('{} must be {}'.format(
				'\'{}\''.format(parameter) if isinstance(parameter, str) else parameter, 
				self.type.__name__,
			))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter

	def __repr__(self):
		if issubclass(self.__class__, IsTypeOf):	
			return '{}({})'.format(
				self.__class__.__name__,
				', '.join([p.__repr__() for p in self.patterns]) if self.patterns and len(self.patterns) else ''
			)
		return '{}({}{})'.format(
			self.__class__.__name__,
			self.type.__name__,
			', ({})'.format(
				', '.join([p.__repr__() for p in self.patterns])
			) if self.patterns and len(self.patterns) else ''
		)


class IsBool(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(bool, patterns=args, error=error)
		return

class IsInteger(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(int, patterns=args, error=error)
		return


class IsFloat(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(float, patterns=args, error=error)
		return


class IsString(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(str, patterns=args, error=error)
		return


class IsList(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(MutableSequence, patterns=args, error=error)
		return


class IsTuple(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(Sequence, patterns=args, error=error)
		return


class IsSet(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(MutableSet, patterns=args, error=error)
		return


class IsFixedSet(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(Set, patterns=args, error=error)
		return


class IsDictionary(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(MutableMapping, patterns=args, error=error)
		return


class IsFixedDictionary(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(Mapping, patterns=args, error=error)
		return


class IsByteArray(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(bytes, patterns=args, error=error)
		return


class IsByteStream(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(bytearray, patterns=args, error=error)
		return
	

class IsDecimal(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(Decimal, patterns=args, error=error)
		return


class ToTypeOf(Pattern):
	def __init__(self, type : type, error: BaseException = None):
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
		if issubclass(self.__class__, ToTypeOf):	
			return '{}()'.format(self.__class__.__name__)
		return '{}({})'.format(self.__class__.__name__, self.type.__name__)
	

class ToBool(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(bool, error)
		return


class ToInteger(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(int, error)
		return


class ToFloat(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(float, error)
		return


class ToString(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(str, error)
		return


class ToList(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(list, error)
		return


class ToTuple(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(tuple, error)
		return
	

class ToSet(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(set, error)
		return


class ToDictionary(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(dict, error)
		return
	

class ToByteArray(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(bytes, error)
		return


class ToByteStream(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(bytearray, error)
		return


class ToDecimal(ToTypeOf):
	def __init__(self, error: BaseException = None):
		super().__init__(Decimal, error)
		return


class IsDataObject(Pattern):
	def __init__(
		self, 
		*patterns: Pattern,
		error: BaseException = None
	):
		self.patterns = patterns if isinstance(patterns, Iterable) else (patterns,)
		self.error = error
		return

	def __call__(self, parameter):
		if not is_dataclass(parameter.__class__):
			if self.error:
				raise self.error
			raise TypeError('{} must be dataclass'.format(
				'\'{}\''.format(parameter) if isinstance(parameter, str) else parameter, 
			))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter	


class IsArray(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter: Sequence) -> Sequence:
		if not isinstance(parameter, Iterable):
			if self.error:
				raise self.error
			raise TypeError('{} must be iterable'.format(parameter))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join([p.__repr__() for p in self.patterns])
		)

