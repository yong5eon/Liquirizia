# -*- coding: utf-8 -*-

from ..DataTypeObject import DataTypeObject
from ..DataTypeObjectFactory import DataTypeObjectFactory

from copy import copy

__all__ = (
	'List'
)


class List(DataTypeObject):
	"""List Data Type Object Class of Data Model Object"""

	def __getitem__(self, key):
		return DataTypeObjectFactory(
			self.__value__.__getitem__(key) if key < len(self.__value__) else None,
			self.__object__,
			self.__model__,
		)

	def __setitem__(self, key, value):
		try:
			prev = copy(self.__model__.__object__.__getitem__(self.__object__.name))
			self.__value__.__setitem__(key, value)
			self.__model__.__object__.__setitem__(
				self.__object__.name,
				self.__object__.validator(self.__value__)
			)
			if self.__object__.callback:
				self.__object__.callback(
					self.__model__, 
					self.__object__.name, 
					self.__model__.__object__.__getitem__(self.__object__.name),
					prev,
				)
		except Exception as e:
			self.__value__ = prev
			self.__model__.__object__.__setitem__(
				self.__object__.name,
				prev
			)
			raise e
		return

	def append(self, value):
		try:
			prev = copy(self.__model__.__object__.__getitem__(self.__object__.name))
			self.__value__.append(value)
			self.__model__.__object__.__setitem__(
				self.__object__.name,
				self.__object__.validator(self.__value__)
			)
			if self.__object__.callback:
				self.__object__.callback(
					self.__model__, 
					self.__object__.name, 
					self.__model__.__object__.__getitem__(self.__object__.name),
					prev,
				)
		except Exception as e:
			self.__value__ = prev
			self.__model__.__object__.__setitem__(
				self.__object__.name,
				prev
			)
			raise e
		return	