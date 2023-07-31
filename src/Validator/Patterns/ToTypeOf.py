# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from collections.abc import Iterable

__all__ = (
	'ToTypeOf',
	'ToBool',
	'ToInteger',
	'ToFloat',
	'ToString',
	'ToList',
	'ToTuple',
	'ToDictionary',
)


class ToTypeOf(Pattern):
	def __init__(self, type : type, error=None):
		self.type = type
		self.error = error
		return

	def __call__(self, parameter):
		try:
			return self.type(parameter)
		except TypeError as e:
			if self.error:
				raise self.error
			raise e

	def __repr__(self):
		return '{}()'.format(self.type.__name__)
	


class ToBool(ToTypeOf):
	def __init__(self, error=None):
		super(ToBool, self).__init__(bool, error)
		return


class ToInteger(ToTypeOf):
	def __init__(self, error=None):
		super(ToInteger, self).__init__(int, error)
		return


class ToFloat(ToTypeOf):
	def __init__(self, error=None):
		super(ToFloat, self).__init__(float, error)
		return


class ToString(ToTypeOf):
	def __init__(self, error=None):
		super(ToString, self).__init__(str, error)
		return


class ToList(ToTypeOf):
	def __init__(self, error=None):
		super(ToList, self).__init__(list, error)
		return


class ToTuple(ToTypeOf):
	def __init__(self, error=None):
		super(ToList, self).__init__(tuple, error)
		return


class ToDictionary(ToTypeOf):
	def __init__(self, error=None):
		super(ToList, self).__init__(dict, error)
		return
