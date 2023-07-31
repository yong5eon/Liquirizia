# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import le

__all__ = (
	'IsLessEqualTo'
)


class IsLessEqualTo(Pattern):
	def __init__(self, compare, error=None):
		self.compare = compare
		self.error = error
		return

	def __call__(self, parameter):
		if not le(parameter, self.compare):
			if self.error:
				raise self.error
			raise ValueError('{} must be less equal to {}'.format(parameter, self.compare))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.compare
		)
