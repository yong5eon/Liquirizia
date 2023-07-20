# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error
from ..Validator import Validator

from collections.abc import Mapping, Iterable

__all__ = (
	'IsMappingOf'
)


class IsMappingOf(Pattern):
	def __init__(
		self, 
		mappings : dict = {}, 
		error    : Error = None
	):
		self.mappings = self.__mapper__(mappings)
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, Mapping):
			if self.error:
				raise self.error(parameter)
			raise TypeError('{} must be dict'.format(parameter))
		if self.mappings:
			for key, validator in self.mappings.items():
				if key in parameter.keys():
					parameter[key] = validator(parameter[key])
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
