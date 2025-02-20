# -*- coding: utf-8 -*-

from .Model import Model
from .Value import Value
from .Handler import Handler

from ..Validator import Validator, Pattern

from typing import Iterable, Dict, Union, Sequence

__all__ = (
	'Model',
	'Value',
	'Handler',
	'IsDataModel',
	'IsRequiredIn',
	'IsMappingOf',
)


class IsDataModel(Pattern):
	def __init__(
		self, 
		*patterns: Pattern,
		error: BaseException = None
	):
		self.patterns = patterns if isinstance(patterns, Iterable) else (patterns,)
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, Model):
			if self.error:
				raise self.error
			raise TypeError('{} must be Model'.format(
				'\'{}\''.format(parameter) if isinstance(parameter, str) else parameter, 
			))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter	


class IsRequiredIn(Pattern):
	def __init__(self, *args, error=None):
		self.args = args
		self.error = error
		return

	def __call__(self, parameter: Model) -> Model:
		if not isinstance(parameter, Model):
			if self.error:
				raise self.error
			raise TypeError('{} must be dataclass'.format(parameter))
		for arg in self.args:
			if not hasattr(parameter, arg):
				if self.error:
					raise self.error
				raise ValueError('{} is required in {}'.format(arg, parameter))
		return parameter

	def __repr__(self) -> str:
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[repr(p) for p in self.args]
			)
		)


class IsMappingOf(Pattern):
	def __init__(
		self, 
		mappings: Dict[str, Union[Validator, Pattern, Sequence[Pattern]]] = {}, 
		error: BaseException = None
	):
		self.mappings = self.__mapper__(mappings)
		self.error = error
		return

	def __call__(self, parameter: Model) -> Model:
		if not isinstance(parameter, Model):
			if self.error:
				raise self.error
			raise TypeError('{} must be based Model'.format(parameter))
		if self.mappings:
			for key, validator in self.mappings.items():
				if not hasattr(parameter, key):
					if self.error:
						raise self.error
					raise ValueError('{} is required in {}'.format(key, parameter))
				setattr(parameter, key, validator(getattr(parameter, key)))
		return parameter

	def __mapper__(self, mappings: Dict[str, Validator]) -> Dict[str, Validator]:
		if not isinstance(mappings, dict):
			raise TypeError('{} must be dict'.format(mappings))
		for key, value in mappings.items():
			if isinstance(value, Sequence):
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

	def __repr__(self) -> str:
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				['{}: {}'.format(k, repr(v)) for k, v in self.mappings.items()]
			)
		)