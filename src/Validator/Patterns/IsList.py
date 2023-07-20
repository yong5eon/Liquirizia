# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'IsList'
)


class IsList(Pattern):
	def __init__(self, *args, error: Error = None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is not None and not isinstance(parameter, list):
			if self.error:
				raise self.error(parameter)
			raise RuntimeError('{} must be list'.format(parameter))
		if parameter is None:
			for pattern in self.patterns:
				parameter = pattern(parameter)
			return parameter
		
		for pattern in self.patterns:
			for index, element in enumerate(parameter):
				parameter[index] = pattern(element)
		
		return parameter
