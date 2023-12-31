# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import lt

__all__ = (
	'IsMinSizeOf'
)


class IsMinSizeOf(Pattern):
	def __init__(self, size : int, error=None):
		self.size = size
		self.error = error
		return

	def __call__(self, parameter):
		if lt(len(parameter), self.size):
			if self.error:
				raise self.error
			raise ValueError('{} must be minium size of {}'.format(
				parameter,
				self.size
			))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.size
		)
