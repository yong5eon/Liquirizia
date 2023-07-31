# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'IsAlphabet'
)


class IsAlphabet(Pattern):
	def __init__(self, error=None):
		self.error = error
		return

	def __call__(self, parameter):
		if not parameter.isalpha():
			if self.error:
				raise self.error
			raise ValueError('{} must be alphabet'.format(parameter))
		return parameter
