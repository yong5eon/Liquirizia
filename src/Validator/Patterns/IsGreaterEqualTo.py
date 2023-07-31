# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import ge

__all__ = (
	'IsGreaterEqualTo'
)


class IsGreaterEqualTo(Pattern):
	def __init__(self, compare, error=None):
		self.compare = compare
		self.error = error
		return

	def __call__(self, parameter):
		if not ge(parameter, self.compare):
			if self.error:
				raise self.error
			raise ValueError('{} must be greater equal to {}'.format(parameter, self.compare))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.compare
		)
