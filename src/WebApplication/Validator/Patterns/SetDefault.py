# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from ...Response import Response

__all__ = (
	'SetDefault'
)


class SetDefault(Pattern):
	def __init__(self, default):
		self.default = default
		return

	def __call__(self, parameter) -> (any, (Response, None)):
		if not parameter:
			return self.default, None
		return parameter, None
