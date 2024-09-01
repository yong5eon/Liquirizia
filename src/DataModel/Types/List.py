# -*- coding: utf-8 -*-

from ..Type import Type

from copy import copy, deepcopy
from collections.abc import Sequence
from typing import Iterator

__all__ = (
	'List'
)


class List(Type, Sequence):
	"""List Data Type Object Class of Data Model Object"""

	def __getattr__(self, name):
		return self.__value__.__getattr__(name)
	
	def __len__(self):
		return self.__value__.__len__()
	
	def __iter__(self) -> Iterator:
		return self.__value__.__iter__()
	
	def __reversed__(self) -> Iterator:
		return self.__value__.__reversed__()

	def __getitem__(self, key):
		return Type.Create(
			self.__value__.__getitem__(key) if key < len(self.__value__) else None,
			self.__attr__,
			self.__model__,
		)

	def __setitem__(self, key, value):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.__setitem__(key, value)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self
	
	def __delitem__(self, key):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.__delitem__(key)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self
	
	def __copy__(self):
		return copy(self.__value__)
	
	def __deepcopy(self):
		return deepcopy(self.__value__)
	
	def __iadd__(self, values):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.__iadd__(values)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self
	
	def insert(self, value):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.insert(value)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self

	def append(self, value):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.append(value)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self
	
	def clear(self):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.clear()
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def reverse(self):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.reverse()
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self
	
	def extend(self, values):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.extend(values)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def remove(self, value):
		pv = deepcopy(self.__value__)
		po = deepcopy(self.__attr__.__getitem__(self.__attr__.name))
		try:
			self.__value__.remove(value)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def pop(self, key: int = -1):
		return Type.Create(
			self.__value__.pop(key),
			self.__attr__,
			self.__model__,
		)
	