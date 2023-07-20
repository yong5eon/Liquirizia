# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'IsElementOf'
)


class IsElementOf(Pattern):
	def __init__(self, *args, error: Error = None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		parameter = list(parameter)
		for pattern in self.patterns:
			for i, e in enumerate(parameter):
				parameter[i] = pattern(e)
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[repr(p) for p in self.patterns]
			)
		)
