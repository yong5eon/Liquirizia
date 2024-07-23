# -*- coding: utf-8 -*-

from Liquirizia.Validator import Validator

from .DataTypeObject import DataTypeObject
from .DataAccessTypeObjectHandler import DataAccessTypeObjectHandler

from copy import deepcopy

__all__ = (
	'DataAccessTypeObject'
)


class DataAccessTypeObject(object):
	"""Data Access Type Object Class of Data Access Model Object"""

	def __init__(
		self, 
		va : Validator = Validator(),
		fn : DataAccessTypeObjectHandler = None
	):
		self.validator = va
		self.callback = fn
		self.name = None 
		self.value = None 
		return

	def __set_name__(self, obj, name):
		self.name = name
		return

	def __init_object__(self, obj, value):
		if obj is None:
			return
		obj.__object__.__setitem__(
			self.name, 
			self.validator(value)
		)
		self.value = deepcopy(value)
		return self

	def __set__(self, obj, value):
		if obj is None:
			return
		obj.__object__.__setitem__(
			self.name, 
			self.validator(value)
		)
		if self.callback:
			self.callback(
				obj,
				self.name,
				obj.__object__.__getitem__(self.name),
			)
		self.value = deepcopy(value)
		return self

	def __get__(self, obj, type=None):
		if obj is None:
			return self
		if self.name not in obj.__object__.keys():
			raise AttributeError('type object \'{}\' has no attribute \'{}\''.format(
				obj.__class__.__name__,
				self.name
			))
		v = obj.__object__.__getitem__(self.name)
		o = DataTypeObject(
			v,
			self,
			obj,
		)	
		self.value = deepcopy(v)
		return o

	def __delete__(self, obj):
		raise ValueError('{} is not able to delete in {}'.format(
			self.name,
			obj.__class__.__name__
		))
