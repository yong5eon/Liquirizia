# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

from collections.abc import Iterable

__all__ = (
	'ToList'
)


class ToList(Pattern):
	def __init__(self, error : Error = None):
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, Iterable):
			if self.error:
				raise self.error(parameter)
			raise TypeError('{} is not iterable'.format(parameter))
		return list(parameter)

	def __repr__(self):
		return '{}()'.format(self.__class__.__name__)
