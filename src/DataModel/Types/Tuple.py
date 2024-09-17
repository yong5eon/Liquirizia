# -*- coding: utf-8 -*-

from ..Type import Type

from collections.abc import Sequence

__all__ = (
	'Tuple'
)


class Tuple(Type, Sequence):
	"""Tuple Data Type Object Class of Data Model Object"""

	# def __getattr__(self, name):
	#	 return self.__value__.__getattr__(name)

	def __contains__(self, value):
		return self.__value__.__contains__(value)
	
	def __len__(self):
		return self.__value__.__len__()
	
	def __iter__(self, name):
		return self.__value__.__iter__()

	def __reserved__(self):
		return self.__value__.__reserved__()

	def __getitem__(self, key):
		return Type.Create(
			self.__value__.__getitem__(key) if key < len(self.__value__) else None,
			self.__attr__,
			self.__model__,
		)

	def index(self, value: any, start: int = 0, stop: int = ...) -> int:
		return self.__value__.index(value, start, stop)

	def count(self, value: any) -> int:
		return self.__value__.count(value)
	
	def __eq__(self, other: any) -> bool:
		if isinstance(other, Tuple): return self.__value__.__eq__(other.__value__)
		return self.__value__.__eq__(other)
	
	def __ne__(self, other: any) -> bool:
		if isinstance(other, Tuple): return self.__value__.__ne__(other.__value__)
		return self.__value__.__ne__(other)