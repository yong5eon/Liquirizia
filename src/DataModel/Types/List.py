# -*- coding: utf-8 -*-

from ..Type import Type

from collections.abc import MutableSequence
from operator import eq, ne
from copy import deepcopy

__all__ = (
	'List'
)


class List(Type, MutableSequence):
	"""List Type Object Class of Data Model"""

	def __iter__(self):
		return self.__value__.__iter__()
	
	def __reversed__(self):
		return self.__value__.__reversed__()
	
	def __len__(self):
		return self.__value__.__len__()
	
	def __contains__(self, value):
		return self.__value__.__contains__(value)

	def __getitem__(self, index):
		return Type.Create(
			self.__value__.__getitem__(index),
			self.__model__,
			self.__descriptor__,
		)

	def __setitem__(self, index, value):
		pv = deepcopy(self.__value__.__getitem__(index)) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.__setitem__(index, value)
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
			self.__value__.__setitem__(index, pv)
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def __delitem__(self, index):
		pv = deepcopy(self.__value__.__getitem__(index)) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.__delitem__(index)
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
			self.__value__.__setitem__(index, pv)
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def __iadd__(self, values):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.__iadd__(values)
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
			self.__value__ = pv
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def index(self, value: any, start: int = 0, stop: int = ...) -> int:
		return self.__value__.index(value, start, stop)
	
	def count(self, value: any) -> int:
		return self.__value__.count(value)
	
	def insert(self, index, value):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.insert(index, value)
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
			self.__value__ = pv
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e

	def append(self, value):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.append(value)
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
			self.__value__ = pv
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def clear(self):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.clear()
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
			self.__value__ = pv
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def reverse(self):
		pv = deepcopy(self.__value__)
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.reverse()
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
			self.__value__ = pv
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def extend(self, values):
		pv = deepcopy(self.__value__)
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.extend(values)
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
			self.__value__ = pv
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def remove(self, value):
		pv = deepcopy(self.__value__)
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.remove(value)
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
			self.__value__ = pv
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def pop(self, index: int = -1):
		pv = deepcopy(self.__value__)
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.pop(index)
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
			self.__value__ = pv
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def __eq__(self, other):
		if isinstance(other, List):
			return eq(self.__value__, other.__value__)
		return eq(self.__value__, other)

	def __ne__(self, other):
		if isinstance(other, List):
			return ne(self.__value__, other.__value__)
		return ne(self.__value__, other)
