# -*- coding: utf-8 -*-

from .Attribute import Attribute

from typing import ItemsView, KeysView, ValuesView

from collections.abc import Iterable, Mapping
from copy import deepcopy

__all__ = (
	'Model'
)


class Model(Mapping):
	"""Abstract Model Class of Data Model"""

	def __new__(cls, **kwargs):
		o = object.__new__(cls)
		o.__object__ = dict()
		for k, v in cls.__dict__.items():
			if isinstance(v, Attribute):
				v.__init_object__(o, kwargs[k] if k in kwargs.keys() else None)
		return o

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.__object__.__repr__()[1:-1]
		)

	def __str__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.__object__.__repr__()[1:-1]
		)

	# implements interface of Container
	def __contains__(self, key: object) -> bool:
		return self.__object__.__contains__(key)
	
	# implements interface of Sized
	def __len__(self):
		return self.__object__.__len__()

	# implements interfaces of Iterable 
	def __iter__(self):
		return self.__object__.__iter__()

	# implements interfaces of Mapping
	def __getitem__(self, key):
		return self.__object__.__getitem__(key)
	
	def keys(self) -> KeysView:
		return self.__object__.keys()
	
	def items(self) -> ItemsView:
		return self.__object__.items()
	
	def values(self) -> ValuesView:
		return self.__object__.values()
	
	def __eq__(self, other: any) -> bool:
		return self.__object__.__eq__(other)
	
	def __ne__(self, other: any) -> bool:
		return self.__object__.__ne__(other)

	# copy
	def __copy__(self):
		return self.__class__.__new__(self.__class__, **self.__object__)

	def __deepcopy__(self, memo={}):
		o = self.__class__.__new__(self.__class__, **self.__object__)
		memo[id(self)] = o
		for k, v in self.__dict__.items():
			setattr(o, k, deepcopy(v, memo))
		return o