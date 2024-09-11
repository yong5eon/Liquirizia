# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import eq

__all__ = (
	'SetDefault',
	'IsToNone',
	'IsNotToNone',
	'IsNotEmpty',
)


class SetDefault(Pattern):
	def __init__(self, default):
		self.default = default
		return

	def __call__(self, parameter):
		if parameter == None:
			return self.default
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.default
		)
	

class IsToNone(Pattern):
	def __init__(self, *args):
		self.patterns = args
		return

	def __call__(self, parameter):
		if parameter is None:
			return parameter
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter


class IsNotToNone(Pattern):
	def __init__(self, error=None):
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is None:
			if self.error:
				raise self.error
			raise ValueError('{} is None'.format(parameter))
		return parameter
	

class IsNotEmpty(Pattern):
	def __init__(self, error=None):
		self.error = error
		return

	def __call__(self, parameter):
		if eq(len(parameter), 0):
			if self.error:
				raise self.error
			raise ValueError('{} must be not empty'.format(parameter))
		return parameter

