# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error
from ..Validator import Validator

__all__ = (
	'IsDictionary'
)


class IsDictionary(Pattern):
	def __init__(self, mappings: dict = {}, error: Error = None):
		self.mappings = self.__mapper__(mappings)
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is not None and not isinstance(parameter, dict):
			if self.error:
				raise self.error(parameter)
			raise RuntimeError('{} must be dict'.format(parameter))
		if self.mappings:
			for key, validator in self.mappings.items():
				parameter[key] = validator(parameter[key] if key in parameter.keys() else None)
		return parameter

	def __mapper__(self, mappings: dict):
		if not isinstance(mappings, dict):
			raise RuntimeError('{} must be dict'.format(mappings))
		for key, value in mappings.items():
			if isinstance(value, (dict,)):
				mappings[key] = Validator(**value)
				continue
			if isinstance(value, (list, tuple,)):
				mappings[key] = Validator(*value)
				continue
			if isinstance(value, Pattern):
				mappings[key] = Validator(value)
				continue
			if isinstance(value, Validator):
				mappings[key] = value
				continue
			raise RuntimeError('invalid mapping table, {} must be dictionary or listable of Patterns, or callable based Pattern'.format(value))
		return mappings
