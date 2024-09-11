# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import ne, le, ge, gt, lt

__all__ = (
	'IsSizeOf'
	'IsSizeIn',
	'IsMaxSizeOf',
	'IsMinSizeOf',
)


class IsSizeOf(Pattern):
	def __init__(self, size : int, error=None):
		self.size = size
		self.error = error
		return

	def __call__(self, parameter):
		if ne(len(parameter), self.size):
			if self.error:
				raise self.error
			raise ValueError(
				'{} must be size of {}'.format(
					parameter, 
					self.size
				)
			)
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.size
		)


class IsSizeIn(Pattern):
	def __init__(self, size : int, min : int = 0, error=None):
		self.size = size
		self.min = min 
		self.error = error
		return

	def __call__(self, parameter):
		if lt(len(parameter), self.min) or gt(len(parameter), self.size):
			if self.error:
				raise self.error
			raise ValueError(
				'{} must be size from {} to {}'.format(
					parameter, 
					self.min,
					self.size,
				)
			)
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.size
		)


class IsMaxSizeOf(Pattern):
	def __init__(self, size : int, error=None):
		self.size = size
		self.error = error
		return

	def __call__(self, parameter):
		if gt(len(parameter), self.size):
			if self.error:
				raise self.error
			raise ValueError('{} must be maxium size of {}'.format(
				parameter,
				self.size
			))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.size
		)
	

class IsMinSizeOf(Pattern):
	def __init__(self, size : int, error=None):
		self.size = size
		self.error = error
		return

	def __call__(self, parameter):
		if lt(len(parameter), self.size):
			if self.error:
				raise self.error
			raise ValueError('{} must be minium size of {}'.format(
				parameter,
				self.size
			))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.size
		)