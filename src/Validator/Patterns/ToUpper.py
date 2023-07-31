# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'ToUpper'
)


class ToUpper(Pattern):
	def __call__(self, parameter):
		return parameter.upper()

	def __repr__(self):
		return '{}()'.format(self.__class__.__name__)
