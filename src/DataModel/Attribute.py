# -*- coding: utf-8 -*-

from Liquirizia.Validator import Validator

from .Handler import Handler
from .Type import Type

__all__ = (
	'Attribute'
)


class Attribute(object):
	"""Attribute Class of Model"""

	def __init__(
		self, 
		va : Validator = Validator(),
		fn : Handler = None
	):
		self.validator = va
		self.callback = fn
		self.name = None 
		self.model = None
		return

	def __set_name__(self, obj, name):
		if obj is None:
			return
		self.name = name
		self.model = obj
		return

	def __init_object__(self, obj, value):
		if obj is None:
			return
		obj.__object__.__setitem__(
			self.name, 
			self.validator(value)
		)
		return self

	def __set__(self, obj, value):
		if obj is None:
			return
		prev = obj.__object__.__getitem__(self.name)
		obj.__object__.__setitem__(
			self.name, 
			self.validator(value)
		)
		if self.callback:
			self.callback(
				obj,
				self,
				obj.__object__.__getitem__(self.name),
				prev,
			)
		return self

	def __get__(self, obj, owner=None):
		if obj is None:
			return self
		if self.name not in obj.__object__.keys():
			raise AttributeError('type object \'{}\' has no attribute \'{}\''.format(
				obj.__class__.__name__,
				self.name
			))
		v = obj.__object__.__getitem__(self.name)
		return Type.Create(v, self, obj)
	
	def __delete__(self, obj):
		raise ValueError('{} is not able to delete in {}'.format(
			self.name,
			obj.__class__.__name__
		))
