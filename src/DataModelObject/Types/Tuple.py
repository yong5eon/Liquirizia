# -*- coding: utf-8 -*-

from ..DataTypeObject import DataTypeObject
from ..DataTypeObjectFactory import DataTypeObjectFactory

__all__ = (
	'Tuple'
)


class Tuple(DataTypeObject):
	"""Tuple Data Type Object Class of Data Model Object"""

	def __getitem__(self, key):
		return DataTypeObjectFactory(
			self.__value__.__getitem__(key) if key < len(self.__value__) else None,
			self.__object__,
			self.__model__,
		)
