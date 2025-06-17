# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import eq, ne, gt, ge, lt, le

__all__ = (
	'IsIn',
	'IsNotIn',
	'IsEqualTo',
	'IsNotEqualTo',
	'IsGreaterThan',
	'IsGreaterEqualTo',
	'IsLessThan',
	'IsLessEqualTo',
)


class IsIn(Pattern):
	def __init__(self, *args, error=None):
		self.compares = args
		self.error = error
		return

	def __call__(self, parameter):
		if parameter not in self.compares:
			if self.error:
				raise self.error
			raise ValueError('{} must be in {}'.format(parameter, self.compares))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[repr(c) for c in self.compares]
			)
		)


class IsNotIn(Pattern):
	def __init__(self, *args, error=None):
		self.compares = args
		self.error = error
		return

	def __call__(self, parameter):
		if parameter in self.compares:
			if self.error:
				raise self.error
			raise ValueError('{} must be not in {}'.format(parameter, self.compares))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[repr(c) for c in self.compares]
			)
		)


class IsEqualTo(Pattern):
	def __init__(self, equal, error=None):
		self.equal = equal
		self.error = error
		return

	def __call__(self, parameter):
		if not eq(parameter, self.equal):
			if self.error:
				raise self.error
			raise ValueError('{} must equal to {}'.format(parameter, self.equal))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.equal
		)


class IsNotEqualTo(Pattern):
	def __init__(self, equal, error=None):
		self.equal = equal
		self.error = error
		return

	def __call__(self, parameter):
		if not ne(parameter, self.equal):
			if self.error:
				raise self.error
			raise ValueError('{} must not equal to {}'.format(parameter, self.equal))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.equal
		)


class IsGreaterEqualTo(Pattern):
	def __init__(self, compare, error=None):
		self.compare = compare
		self.error = error
		return

	def __call__(self, parameter):
		if not ge(parameter, self.compare):
			if self.error:
				raise self.error
			raise ValueError('{} must be greater equal to {}'.format(parameter, self.compare))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.compare
		)


class IsGreaterThan(Pattern):
	def __init__(self, compare, error=None):
		self.compare = compare
		self.error = error
		return

	def __call__(self, parameter):
		if not gt(parameter, self.compare):
			if self.error:
				raise self.error
			raise ValueError('{} must be greater than {}'.format(parameter, self.compare))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.compare
		)


class IsLessEqualTo(Pattern):
	def __init__(self, compare, error=None):
		self.compare = compare
		self.error = error
		return

	def __call__(self, parameter):
		if not le(parameter, self.compare):
			if self.error:
				raise self.error
			raise ValueError('{} must be less equal to {}'.format(parameter, self.compare))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.compare
		)


class IsLessThan(Pattern):
	def __init__(self, compare, error=None):
		self.compare = compare
		self.error = error
		return

	def __call__(self, parameter):
		if not lt(parameter, self.compare):
			if self.error:
				raise self.error
			raise ValueError('{} must be less than {}'.format(parameter, self.compare))
		return parameter

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.compare
		)