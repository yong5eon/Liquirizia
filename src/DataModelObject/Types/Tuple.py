# -*- coding: utf-8 -*-

from ..DataTypeObject import DataTypeObject
from ..DataTypeObjectFactory import DataTypeObjectFactory

__all__ = (
	'Tuple'
)


class Tuple(DataTypeObject):
	"""Tuple Data Type Object Class of Data Model Object"""

	def __getattr__(self, name):
		return self.__value__.__getattr__(name)
	
	def __iter__(self, name):
		return self.__value__.__iter__()

	def __getitem__(self, key):
		return DataTypeObjectFactory(
			self.__value__.__getitem__(key) if key < len(self.__value__) else None,
			self.__attr__,
			self.__model__,
		)

