# -*- coding: utf-8 -*-

from Liquirizia.Validator import Validator

from .Handler import Handler
from .Type import Type
from .Format import (
	Boolean,
	Integer,
	Number,
	String,
	Array,
	Object,
	OneOf,
)

from typing import Any, Union

__all__ = (
	'Value'
)


class Value(object):
	"""Value Class of Model"""

	def __init__(
		self,
		va : Validator = Validator(),
		default: Any = None,
		description: str = None,
		format: Union[Boolean, Integer, Number, String, Array, Object, OneOf] = None,
		fn : Handler = None,
	):
		self.model = None
		self.name = None 
		self.validator = va
		self.default = default
		self.description = description
		self.format = format
		self.callback = fn
		return
	
	def __repr__(self):
		return '{}(default={}, description=\'{}\', valdator={}, callback={})'.format(
			self.__class__.__name__,
			'\'{}\''.format(self.default) if isinstance(self.default, str) else self.default,
			self.description,
			self.validator,
			self.callback,
		)

	def __set_name__(self, obj, name):
		if obj is None:
			return
		self.model = obj
		self.name = name
		return
	
	def __set__(self, obj, value, init: bool = False):
		if obj is None:
			return
		ex = self.name in obj.__properties__.keys()
		pv = obj.__properties__[self.name] if ex else None
		try:
			if self.validator:
				value = self.validator(value.__value__ if isinstance(value, Type) else value)
			obj.__properties__[self.name] = value
			if not init and self.callback:
				self.callback(
					obj,
					self,
					obj.__properties__[self.name],
					pv,
				)
			if not init and obj.__callback__:
				obj.__callback__(
					obj,
					self,
					obj.__properties__[self.name],
					pv,
				)
			return 
		except Exception as e:
			if ex:
				obj.__properties__[self.name] = pv
			raise e

	def __get__(self, obj, owner=None):
		if obj is None:
			return self
		if self.name not in obj.__properties__.keys():
			return self.default
		_ = obj.__properties__[self.name]
		return Type.Create(_, obj, self)
	
	def __delete__(self, obj):
		raise ValueError('{} is not able to delete in {}'.format(
			self.name,
			obj.__class__.__name__
		))
