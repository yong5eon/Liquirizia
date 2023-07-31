# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'IsNotToNone'
)


class IsNotToNone(Pattern):
	def __init__(self, error=None):
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is None:
			if self.error:
				raise self.error
			raise ValueError('{} is None'.format(parameter))
		return parameter
