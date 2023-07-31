# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'IsNumeric'
)


class IsNumeric(Pattern):
	def __init__(self, error=None):
		self.error = error
		return

	def __call__(self, parameter):
		if not parameter.isnumeric():
			if self.error:
				raise self.error
			raise ValueError('{} must be numeric'.format(parameter))
		return parameter
