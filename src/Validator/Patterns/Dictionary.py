# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Validator import Validator

from collections.abc import Mapping

__all__ = (
	'IsRequiredIn',
	'IsMappingOf',
	'IsKeyOf',
	'IsValueOf',
)


class IsRequiredIn(Pattern):
	def __init__(self, *args, error=None):
		self.args = args
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, Mapping):
			if self.error:
				raise self.error
			raise TypeError('{} must be dict'.format(parameter))
		keys = parameter.keys()
		for arg in self.args:
			if arg not in keys:
				if self.error:
					raise self.error
				raise ValueError('{} is required in {}'.format(arg, parameter))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[repr(p) for p in self.args]
			)
		)


class IsMappingOf(Pattern):
	def __init__(
		self, 
		mappings : dict = {}, 
		error		   = None
	):
		self.mappings = self.__mapper__(mappings)
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, Mapping):
			if self.error:
				raise self.error
			raise TypeError('{} must be dict'.format(parameter))
		if self.mappings:
			for key, validator in self.mappings.items():
				parameter[key] = validator(parameter[key] if key in parameter.keys() else None)
		return parameter

	def __mapper__(self, mappings: dict):
		if not isinstance(mappings, dict):
			raise TypeError('{} must be dict'.format(mappings))
		for key, value in mappings.items():
			if isinstance(value, (dict,)):
				mappings[key] = Validator(**value)
				continue
			if isinstance(value, (list, tuple)):
				mappings[key] = Validator(*value)
				continue
			if isinstance(value, Pattern):
				mappings[key] = Validator(value)
				continue
			if isinstance(value, Validator):
				mappings[key] = value
				continue
			raise ValueError('Invalid mapping table, {} must be dictionary or listable of Patterns, or callable based Pattern'.format(value))
		return mappings

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				['{}: {}'.format(k, repr(v)) for k, v in self.mappings.items()]
			)
		)


class IsKeyOf(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, Mapping):
			if self.error:
				raise self.error
			raise TypeError('{} must be dict'.format(parameter))
		try:
			for k, v in parameter.items():
				for pattern in self.patterns:
					k = pattern(k)
				parameter[k] = v
			return parameter
		except Exception as e:
			if self.error:
				raise self.error
			raise e

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[repr(p) for p in self.patterns]
			)
		)


class IsValueOf(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, Mapping):
			if self.error:
				raise self.error
			raise TypeError('{} must be dict'.format(parameter))
		try:
			for k, v in parameter.items():
				for pattern in self.patterns:
					v = pattern(v)
				parameter[k] = v
			return parameter
		except Exception as e:
			if self.error:
				raise self.error
			raise e

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[repr(p) for p in self.patterns]
			)
		)
