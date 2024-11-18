# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from collections.abc import Iterable

__all__ = (
	'IsElementOf',
	'IsArray',
)


class IsArray(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, Iterable):
			if self.error:
				raise self.error
			raise TypeError('{} must be iterable'.format(parameter))
		if parameter is None:
			for pattern in self.patterns:
				parameter = pattern(parameter)
			return parameter
		return parameter


class IsElementOf(Pattern):
	def __init__(self, *args):
		self.patterns = args
		return

	def __call__(self, parameter):
		_ = list(parameter)
		for pattern in self.patterns:
			for i, e in enumerate(_):
				_[i] = pattern(e)
		return type(parameter)(_)

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[repr(p) for p in self.patterns]
			)
		)
