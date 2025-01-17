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

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join([p.__repr__() for p in self.patterns])
		)


class IsNotToNone(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is None:
			if self.error:
				raise self.error
			raise ValueError('{} is None'.format(parameter))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join([p.__repr__() for p in self.patterns])
		)


class IsNotEmpty(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if eq(len(parameter), 0):
			if self.error:
				raise self.error
			raise ValueError('{} must be not empty'.format(parameter))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join([p.__repr__() for p in self.patterns])
		)

