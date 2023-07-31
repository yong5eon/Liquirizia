# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import eq

__all__ = (
	'IsNotEmpty'
)


class IsNotEmpty(Pattern):
	def __init__(self, error=None):
		self.error = error
		return

	def __call__(self, parameter):
		if eq(len(parameter), 0):
			if self.error:
				raise self.error
			raise ValueError('{} must be not empty'.format(parameter))
		return parameter
