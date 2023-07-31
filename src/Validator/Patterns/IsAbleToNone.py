# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'IsAbleToNone'
)


class IsAbleToNone(Pattern):
	def __init__(self, *args):
		self.patterns = args
		return

	def __call__(self, parameter):
		if parameter is None:
			return parameter
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter
