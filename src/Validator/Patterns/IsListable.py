# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from collections.abc import Iterable

__all__ = (
	'IsListable'
)


class IsListable(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, Iterable):
			if self.error:
				raise self.error
			raise TypeError('{} must be listable'.format(parameter))
		if parameter is None:
			for pattern in self.patterns:
				parameter = pattern(parameter)
			return parameter
		return parameter
