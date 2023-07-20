# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'IsIn'
)


class IsIn(Pattern):
	def __init__(self, *args, error: Error = None):
		self.compares = args
		self.error = error
		return

	def __call__(self, parameter):
		if parameter not in self.compares:
			if self.error:
				raise self.error(parameter, self.compares)
			raise ValueError('{} must be in {}'.format(parameter, self.compares))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[repr(c) for c in self.compares]
			)
		)
