# -*- coding: utf-8 -*-

from ..Type import Type

from collections.abc import MutableSet
from operator import eq, ne
from copy import deepcopy

__all__ = (
	'Set'
)


class Set(Type, MutableSet):
	"""Set Type Object Class of Data Model"""

	def __iter__(self):
		return self.__value__.__iter__()

	def __contains__(self, value):
		return self.__value__.__contains__(value)
	
	def __len__(self):
		return self.__value__.__len__()
	
	def __le__(self, other):
		return self.__value__.__le__(other)
	
	def __lt__(self, other):
		return self.__value__.__lt__(other)
	
	def __eq__(self, other):
		return self.__value__.__eq__(other)
	
	def __ne__(self, value):
		return self.__value__.__ne__(value)
	
	def __gt__(self, other):
		return self.__value__.__gt__(other)
	
	def __ge__(self, other):
		return self.__value__.__ge__(other)
	
	def __and__(self, other):
		return self.__value__.__and__(other)
	
	def __or__(self, other):
		return self.__value__.__or__(other)
	
	def __sub__(self, other):
		return self.__value__.__sub__(other)
	
	def __xor__(self, other):
		return self.__value__.__xor__(other)
	
	def isdisjoin(self, s):
		return self.__value__.isdisjoint(s)
	
	def __ior__(self, it):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.__ior__(it)
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
	
	def __iand__(self, it):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.__iand__(it)
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
	
	def __ixor__(self, it):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.__ixor__(it)
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
	
	def __isub__(self, it):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.__isub__(it)
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
	
	def add(self, value):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.add(value)
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
	
	def pop(self):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.pop()
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
	
	def discard(self, value):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.discard(value)
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
		if isinstance(other, Set):
			return eq(self.__value__, other.__value__)
		return eq(self.__value__, other)

	def __ne__(self, other):
		if isinstance(other, Set):
			return ne(self.__value__, other.__value__)
		return ne(self.__value__, other)
