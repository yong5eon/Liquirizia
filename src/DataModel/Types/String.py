# -*- coding: utf-8 -*-

from ..Type import Type

from operator import *

__all__ = (
	'String'
)


class String(Type):
	"""String Data Type Object Class of Data Model Object"""

	def __getattr__(self, name):
		return self.__value__.__getattr__(name)
	
	def __iter__(self):
		return self.__value__.__iter__()

	# calculate operand
	def __add__(self, other):
		return add(self.__value__, other.__value__ if isinstance(other, Type) else other)

	def __mul__(self, other):
		return mul(self.__value__, other.__value__ if isinstance(other, Type) else other)

	def __mod__(self, other):
		return mod(self.__value__, other.__value__ if isinstance(other, Type) else other)

	# compares
	def __lt__(self, other):
		return lt(self.__value__, other.__value__ if isinstance(other, Type) else other)

	def __le__(self, other):
		return le(self.__value__, other.__value__ if isinstance(other, Type) else other)

	def __eq__(self, other):
		return eq(self.__value__, other.__value__ if isinstance(other, Type) else other)

	def __ne__(self, other):
		return ne(self.__value__, other.__value__ if isinstance(other, Type) else other)

	def __ge__(self, other):
		return ge(self.__value__, other.__value__ if isinstance(other, Type) else other)

	def __gt__(self, other):
		return gt(self.__value__, other.__value__ if isinstance(other, Type) else other)

