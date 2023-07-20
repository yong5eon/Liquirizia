# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'IsBool'
)


class IsBool(Pattern):
	def __init__(self, *args, error: Error = None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is not None and not isinstance(parameter, bool):
			if self.error:
				raise self.error(parameter)
			raise RuntimeError('{} must be bool'.format(parameter))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter
