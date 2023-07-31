# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import gt

__all__ = (
	'IsMaxSizeOf'
)


class IsMaxSizeOf(Pattern):
	def __init__(self, size : int, error=None):
		self.size = size
		self.error = error
		return

	def __call__(self, parameter):
		if gt(len(parameter), self.size):
			if self.error:
				raise self.error
			raise ValueError('{} must be maxium size of {}'.format(
				parameter,
				self.size
			))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.size
		)
