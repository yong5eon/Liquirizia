# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import ne

__all__ = (
	'IsSizeOf'
)


class IsSizeOf(Pattern):
	def __init__(self, size : int, error=None):
		self.size = size
		self.error = error
		return

	def __call__(self, parameter):
		if ne(len(parameter), self.size):
			if self.error:
				raise self.error
			raise ValueError(
				'{} must be size of {}'.format(
					parameter, 
					self.size
				)
			)
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.size
		)
