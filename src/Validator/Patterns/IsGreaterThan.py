# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'IsGreaterThan'
)


class IsGreaterThan(Pattern):
	def __init__(self, compare, error: Error = None):
		self.compare = compare
		self.error = error
		return

	def __call__(self, parameter):
		if not parameter > self.compare:
			if self.error:
				raise self.error(parameter, self.compare)
			raise ValueError('{} must be greater than {}'.format(parameter, self.compare))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.compare
		)
