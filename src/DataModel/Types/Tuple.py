# -*- coding: utf-8 -*-

from ..Type import Type

from collections.abc import Sequence
from operator import eq, ne

__all__ = (
	'Tuple'
)


class Tuple(Type, Sequence):
	"""Tuple Type Object Class of Data Model"""

	def __contains__(self, value):
		return self.__value__.__contains__(value)
	
	def __len__(self):
		return self.__value__.__len__()

	def __iter__(self):
		return self.__value__.__iter__()

	def __reversed__(self):
		return self.__value__.__reversed__()

	def __getitem__(self, index):
		return Type.Create(
			self.__value__.__getitem__(index),
			self.__model__,
			self.__descriptor__,
		)

	def index(self, value: any, start: int = 0, stop: int = ...) -> int:
		return self.__value__.index(value, start, stop)

	def count(self, value: any) -> int:
		return self.__value__.count(value)

	def __eq__(self, other):
		if isinstance(other, Tuple):
			return eq(self.__value__, other.__value__)
		return eq(self.__value__, other)

	def __ne__(self, other):
		if isinstance(other, Tuple):
			return ne(self.__value__, other.__value__)
		return ne(self.__value__, other)
