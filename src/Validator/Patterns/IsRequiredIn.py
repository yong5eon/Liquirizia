# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from collections.abc import Mapping

__all__ = (
	'IsRequiredIn'
)


class IsRequiredIn(Pattern):
	def __init__(self, *args, error=None):
		self.args = args
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, Mapping):
			if self.error:
				raise self.error
			raise TypeError('{} must be dict'.format(parameter))
		keys = parameter.keys()
		for arg in self.args:
			if arg not in keys:
				if self.error:
					raise self.error
				raise ValueError('{} is required in {}'.format(arg, parameter))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[repr(p) for p in self.args]
			)
		)

