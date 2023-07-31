# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'ToLower'
)


class ToLower(Pattern):
	def __call__(self, parameter):
		return parameter.lower()

	def __repr__(self):
		return '{}()'.format(self.__class__.__name__)
