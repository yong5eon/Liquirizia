# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'If',
)


class If(Pattern):
	def __init__(self, *args, error=None) -> None:
		self.patterns = args
		self.error = error
		return
	
	def __call__(self, parameter):
		try:
			for pattern in self.patterns:
				parameter = pattern(parameter)
			return parameter
		except Exception:
			return parameter