# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import eq

__all__ = (
	'IsEqualTo'
)


class IsEqualTo(Pattern):
	def __init__(self, equal, error=None):
		self.equal = equal
		self.error = error
		return

	def __call__(self, parameter):
		if not eq(parameter, self.equal):
			if self.error:
				raise self.error
			raise ValueError('{} must equal to {}'.format(parameter, self.equal))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.equal
		)
