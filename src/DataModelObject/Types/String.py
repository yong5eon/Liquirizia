# -*- coding: utf-8 -*-

from ..DataTypeObject import DataTypeObject
from ..DataTypeObjectFactory import DataTypeObjectFactory

from operator import *

__all__ = (
	'String'
)


class String(DataTypeObject):
	"""String Data Type Object Class of Data Model Object"""

	def __getitem__(self, key):
		return DataTypeObjectFactory(
			self.__value__.__getitem__(key) if key < len(self.__value__) else None,
			self.__object__,
			self.__model__,
		)

	def __len__(self):
		return len(self.__value__)
	
	def __sizeof__(self):
		return self.__value__.__sizeof__()

	# calculate operand
	def __add__(self, other):
		return add(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __mul__(self, other):
		return mul(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __mod__(self, other):
		return mod(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	# compares
	def __lt__(self, other):
		return lt(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __le__(self, other):
		return le(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __eq__(self, other):
		return eq(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __ne__(self, other):
		return ne(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __ge__(self, other):
		return ge(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __gt__(self, other):
		return gt(self.__value__, other.v if isinstance(other, DataTypeObject) else other)
	