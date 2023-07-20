# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'ToLower'
)


class ToLower(Pattern):
	def __init__(self, error : Error = None):
		self.error = error
		return

	def __call__(self, parameter):
		return parameter.lower()

	def __repr__(self):
		return '{}()'.format(self.__class__.__name__)
