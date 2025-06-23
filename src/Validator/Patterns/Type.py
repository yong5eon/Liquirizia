# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from decimal import Decimal
from dataclasses import is_dataclass, make_dataclass
from collections.abc import (
	Iterable,
	Mapping,
)
from typing import Type, Sequence, Union

__all__ = (
	'IsTypeOf',
	'IsBool',
	'IsInteger',
	'IsFloat',
	'IsNumber',
	'IsString',
	'IsList',
	'IsTuple',
	'IsSet',
	'IsArray',
	'IsObject',
	'IsByteString',
	'IsByteArray',
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
	'ToObject',
	'ToByteString',
	'ToByteArray',
	'ToDecimal',
	'ToDataObject',
)


class IsTypeOf(Pattern):
	def __init__(
		self, 
		type: Union[Type, Sequence[Type]],
		patterns: Sequence[Pattern] = (),
		error: BaseException = None
	):
		self.type = type
		self.patterns = patterns if isinstance(patterns, Iterable) else (patterns,)
		self.error = error
		return

	def __call__(self, parameter):
		if type(parameter) is not self.type:
			if self.error:
				raise self.error
			raise TypeError('{} must be {}'.format(
				'\'{}\''.format(parameter) if isinstance(parameter, str) else parameter, 
				', '.join([t.__name__ for t in self.type]) if isinstance(self.type, Iterable) else self.type.__name__
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


class IsNumber(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__((int, float), patterns=args, error=error)
		return


class IsString(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(str, patterns=args, error=error)
		return


class IsList(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(list, patterns=args, error=error)
		return


class IsTuple(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(tuple, patterns=args, error=error)
		return


class IsSet(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(set, patterns=args, error=error)
		return


class IsArray(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter: Iterable) -> Iterable:
		if not isinstance(parameter, Iterable) or isinstance(parameter, (str, bytes)):
			if self.error:
				raise self.error
			raise TypeError('{} must be a non-string, non-bytes iterable'.format(parameter))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join([p.__repr__() for p in self.patterns])
		)


class IsObject(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(dict, patterns=args, error=error)
		return


class IsByteString(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(bytes, patterns=args, error=error)
		return


class IsByteArray(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(bytearray, patterns=args, error=error)
		return
	

class IsDecimal(IsTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(Decimal, patterns=args, error=error)
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

	def __call__(self, parameter: object) -> object:
		if not is_dataclass(parameter.__class__):
			if self.error:
				raise self.error
			raise TypeError('{} must be dataclass'.format(
				'\'{}\''.format(parameter) if isinstance(parameter, str) else parameter, 
			))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter	


class ToTypeOf(Pattern):
	def __init__(
		self,
		type : type,
		patterns: Sequence[Pattern] = (),
		error: BaseException = None,
		eval: bool = False,
	):
		self.type = type
		self.patterns = patterns if isinstance(patterns, Iterable) else (patterns,)
		self.error = error
		self.eval = eval
		return

	def __call__(self, parameter):
		try:
			if self.eval:
				parameter = self.type(
					eval(str(parameter)) if not isinstance(parameter, str) else eval(parameter)
				)
			else:
				parameter = self.type(parameter)
		except Exception as e:
			if self.error:
				raise self.error
			raise ValueError('{} cannot be converted to {}'.format(
				'\'{}\''.format(parameter) if isinstance(parameter, str) else parameter, 
				self.type.__name__,
			))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter

	def __repr__(self):
		if issubclass(self.__class__, ToTypeOf):	
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


class ToBool(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(bool, patterns=args, error=error, eval=True)
		return


class ToInteger(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(int, patterns=args, error=error, eval=True)
		return


class ToFloat(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(float, patterns=args, error=error, eval=True)
		return


class ToString(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(str, patterns=args, error=error)
		return


class ToList(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(list, patterns=args, error=error)
		return


class ToTuple(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(tuple, patterns=args, error=error)
		return
	

class ToSet(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(set, patterns=args, error=error)
		return


class ToObject(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(dict, patterns=args, error=error)
		return


class ToByteString(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(bytes, patterns=args, error=error)
		return


class ToByteArray(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(bytearray, patterns=args, error=error)
		return


class ToDecimal(ToTypeOf):
	def __init__(self, *args, error: BaseException = None):
		super().__init__(Decimal, patterns=args, error=error)
		return


class ToDataObject(Pattern):
	def __init__(
		self, 
		*patterns: Pattern,
		error: BaseException = None
	):
		self.patterns = patterns if isinstance(patterns, Iterable) else (patterns,)
		self.error = error
		return

	def __call__(self, parameter: Mapping) -> object:
		try:
			parameter = make_dataclass(
				'DynamicDataClass',
				[(key, type(value)) for key, value in parameter.items()]
			)(**parameter)
		except Exception as e:
			if self.error:
				raise self.error
			raise ValueError('{} cannot be converted to dataclass'.format(
				'\'{}\''.format(parameter) if isinstance(parameter, str) else parameter
			))
		if not is_dataclass(parameter.__class__):
			if self.error:
				raise self.error
			raise TypeError('{} must be dataclass'.format(
				'\'{}\''.format(parameter) if isinstance(parameter, str) else parameter, 
			))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter
