# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from datetime import datetime, date, time

__all__ = (
	'IsDateTime',
	'IsDate',
	'IsTime',
)


class IsDateTime(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is not None and not isinstance(parameter, datetime):
			if self.error:
				raise self.error
			raise RuntimeError('{} must be datetime'.format(parameter))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter


class IsDate(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is not None and not isinstance(parameter, date):
			if self.error:
				raise self.error
			raise RuntimeError('{} must be date'.format(parameter))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter


class IsTime(Pattern):
	def __init__(self, *args, error=None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if parameter is not None and not isinstance(parameter, time):
			if self.error:
				raise self.error
			raise RuntimeError('{} must be time'.format(parameter))
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter