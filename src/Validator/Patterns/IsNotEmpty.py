# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

from operator import eq

__all__ = (
	'IsNotEmpty'
)


class IsNotEmpty(Pattern):
	def __init__(self, error: Error = None):
		self.error = error
		return

	def __call__(self, parameter):
		if eq(len(parameter), 0):
			if self.error:
				raise self.error(parameter, self.size)
			raise ValueError('{} must be not empty'.format(parameter))
		return parameter
