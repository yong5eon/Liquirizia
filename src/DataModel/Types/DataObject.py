# -*- coding: utf-8 -*-

from ..Type import Type

from copy import deepcopy

from typing import Any

__all__ = (
	'DataObject'
)


class Function(object):
	def __init__(self, fn, obj, descriptor):
		self.fn = fn
		self.model = obj
		self.descriptor = descriptor
		return
	def __call__(self, *args, **kwargs):
		po = deepcopy(self.model.__properties__.__getitem__(self.descriptor.name))
		try:
			v = self.fn(*args, **kwargs)
			if self.descriptor.validator:
				self.model.__properties__.__setitem__(
					self.descriptor.name,
					self.descriptor.validator(self.model.__properties__.__getitem__(self.descriptor.name))
				)
			if self.descriptor.callback:
				self.descriptor.callback(
					self.model,
					self.descriptor,
					self.model.__properties__.__getitem__(self.descriptor.name),
					po
				)
			if self.model.__callback__:
				self.model.__callback__(
					self.model,
					self.descriptor,
					self.model.__properties__.__getitem__(self.descriptor.name),
					po
				)
			return v
		except Exception as e:
			self.model.__properties__.__setitem__(
				self.descriptor.name,
				po,
			)
			raise e
		

class DataObject(Type):
	"""DataObject(Data Class) Type Object Class of Data Model Object"""

	def __getattr__(self, key):
		if key in ('__value__', '__model__', '__descriptor__'):
			return super().__getattr__(key)
		_ = getattr(self.__value__, key)
		if callable(_): return Function(_, self.__model__, self.__descriptor__)
		return Type.Create(
			_,
			self.__model__,
			self.__descriptor__,
		)

	def __setattr__(self, key, value):
		if key in ('__value__', '__model__', '__descriptor__'):
			return super().__setattr__(key, value)
		pv = deepcopy(getattr(self.__value__, key))
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = setattr(self.__value__, key, value)
			if self.__descriptor__.validator:
				self.__model__.__properties__.__setitem__(
					self.__descriptor__.name,
					self.__descriptor__.validator(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
				)
			if self.__descriptor__.callback:
				self.__descriptor__.callback(
					self.__model__,
					self.__descriptor__,
					self.__model__.__properties__.__getitem__(self.__descriptor__.name),
					po
				)
			if self.__model__.__callback__:
				self.__model__.__callback__(
					self.__model__,
					self.__descriptor__,
					self.__model__.__properties__.__getitem__(self.__descriptor__.name),
					po
				)
			return v
		except Exception as e:
			setattr(self.__value__, key, pv)
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e

	def __eq__(self, other):
		if isinstance(other, DataObject):
			return self.__value__.__eq__(other.__value__)
		return self.__value__.__eq__(other)
	
	def __ne__(self, other):
		if isinstance(other, DataObject):
			return self.__value__.__ne__(other.__value__)
		return self.__value__.__ne__(other)
	
