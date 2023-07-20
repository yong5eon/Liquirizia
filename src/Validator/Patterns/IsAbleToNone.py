# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'IsAbleToNone'
)


class IsAbleToNone(Pattern):
	def __init__(self, *args, error: Error = None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is None:
			return parameter
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter
