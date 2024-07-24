# -*- coding: utf-8 -*-

from ..Type import Type
from ..TypeFactory import TypeFactory

from copy import deepcopy

__all__ = (
	'Dictionary'
)


class Dictionary(Type):
	"""Dictionary Data Type Object Class of Data Model Object"""

	def __getattr__(self, name):
		return self.__value__.__getattr__(name)
	
	def __iter__(self):
		return self.__value__.__iter__()

	def __getitem__(self, key):
		return TypeFactory(
			self.__value__.__getitem__(key) if key in self.__value__.keys() else None,
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
					self.__attr__.name, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
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
					self.__attr__.name, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def clear(self) -> None:
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
					self.__attr__.name, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def update(self, other):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__attr__.__getitem__(self.__attr__.name))
			self.__value__.update(other)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__.name, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
