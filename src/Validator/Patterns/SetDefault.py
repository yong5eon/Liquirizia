# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'SetDefault'
)


class SetDefault(Pattern):
	def __init__(self, default):
		self.default = default
		return

	def __call__(self, parameter):
		if not parameter:
			return self.default
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.default
		)
