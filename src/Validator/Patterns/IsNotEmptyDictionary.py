# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'IsNotEmptyDictionary'
)


class IsNotEmptyDictionary(Pattern):
	def __init__(self, error: Error = None):
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, dict):
			if self.error:
				raise self.error(parameter)
			raise RuntimeError('{} is not dictionary'.format(parameter))
		if len(parameter.items()) == 0:
			if self.error:
				raise self.error(parameter)
			raise RuntimeError('{} is empty'.format(parameter))
		return parameter
