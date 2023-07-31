# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'IsAlphaNumeric'
)


class IsAlphaNumeric(Pattern):
	def __init__(self, error=None):
		self.error = error
		return

	def __call__(self, parameter):
		if not parameter.isalnum():
			if self.error:
				raise self.error
			raise ValueError('{} must be alphanumeric'.format(parameter))
		return parameter
