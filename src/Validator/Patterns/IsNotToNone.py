# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'IsNotToNone'
)


class IsNotToNone(Pattern):
	def __init__(self, error: Error = None):
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is None:
			if self.error:
				raise self.error(parameter)
			raise ValueError('{} is None'.format(parameter))
		return parameter
