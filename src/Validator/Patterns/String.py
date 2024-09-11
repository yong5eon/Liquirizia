# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'IsAlphabet',
	'IsAlphaNumeric',
	'IsNumeric',
	'ToUpper',
	'ToLower',
)


class IsAlphabet(Pattern):
	def __init__(self, error=None):
		self.error = error
		return

	def __call__(self, parameter):
		if not parameter.isalpha():
			if self.error:
				raise self.error
			raise ValueError('{} must be alphabet'.format(parameter))
		return parameter


class IsAlphaNumeric(Pattern):
	def __init__(self, error=None):
		self.error = error
		return

	def __call__(self, parameter):
		if not parameter.isalnum():
			if self.error:
				raise self.error
			raise ValueError('{} must be alphanumeric'.format(parameter))
		return parameter
	

class IsNumeric(Pattern):
	def __init__(self, error=None):
		self.error = error
		return

	def __call__(self, parameter):
		if not parameter.isnumeric():
			if self.error:
				raise self.error
			raise ValueError('{} must be numeric'.format(parameter))
		return parameter


class ToUpper(Pattern):
	def __call__(self, parameter):
		return parameter.upper()

	def __repr__(self):
		return '{}()'.format(self.__class__.__name__)


class ToLower(Pattern):
	def __call__(self, parameter):
		return parameter.lower()

	def __repr__(self):
		return '{}()'.format(self.__class__.__name__)