# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from operator import eq

__all__ = (
	'IsAlphabet',
	'IsAlphaNumeric',
	'IsNumeric',
	'ToUpper',
	'ToLower',
	'IsSubString',
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


class IsSubString(Pattern):
	def __init__(self, match: str, end: int = None, start: int = 0, error=None):
		self.error = error
		self.match = match
		self.start = start
		self.end = end if end else len(match)
		return
	
	def __call__(self, parameter):
		if not eq(parameter[self.start:self.end], self.match):
			if self.error:
				raise self.error
			raise ValueError('{} is not substring to {}'.format(parameter[self.start:self.end], self.match))
		return parameter
