# -*- coding: utf-8 -*-

from Liquirizia.Validator import Validator

from typing import Any

__all__ = (
	'Value'
)


class Value(object):
	"""Value Class of Configuration"""

	def __init__(
		self, 
		key: str,
		default: Any = None,
		va : Validator = Validator(),
	):
		self.key = key
		self.default = default
		self.validator = va
		self.name = None 
		return

	def __set_name__(self, obj, name):
		if obj is None:
			return
		self.name = name
		return

	def __create__(self, obj, value):
		if obj is None:
			return
		obj.__properties__.__setitem__(
			self.name, 
			self.validator(value)
		)
		return self

	def __set__(self, obj, value):
		if obj is None:
			return
		obj.__properties__.__setitem__(
			self.name, 
			self.validator(value)
		)
		return self

	def __get__(self, obj, owner=None):
		if obj is None:
			return self
		if self.name not in obj.__properties__.keys():
			raise AttributeError('{} has no attribute {}'.format(
				obj.__class__.__name__,
				self.name
			))
		return obj.__properties__.__getitem__(self.name)

	def __delete__(self, obj):
		raise ValueError('{} is not able to delete in {}'.format(
			self.name,
			obj.__class__.__name__
		))
