# -*- coding: utf-8 -*-

from ..DataTypeObject import DataTypeObject

from operator import *

__all__ = (
	'Integer'
)


class Integer(DataTypeObject):
	"""Integer Data Type Object Class of Data Model Object"""

	# type casting
	def __bool__(self):
		return bool(self.__value__)

	def __int__(self):
		return int(self.__value__)

	def __float__(self):
		return float(self.__value__)

	# calculate operand
	def __abs__(self):
		return abs(self.__value__)

	def __add__(self, other):
		return add(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __sub__(self, other):
		return sub(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __mul__(self, other):
		return mul(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __matmul__(self, other):
		return matmul(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __truediv__(self, other):
		return truediv(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __floordiv__(self, other):
		return floordiv(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __mod__(self, other):
		return mod(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __pow__(self, power, modulo=None):
		return pow(self.__value__, power, modulo=modulo)

	# operator magic
	def __neg__(self):
		return neg(self.__value__)

	def __pos__(self):
		return pos(self.__value__)

	def __invert__(self):
		return invert(self.__value__)

	# bit operand
	def __rshift__(self, other):
		return rshift(self.__value__, other)

	def __lshift__(self, other):
		return lshift(self.__value__, other)

	def __and__(self, other):
		return and_(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __or__(self, other):
		return or_(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __xor__(self, other):
		return xor(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

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
