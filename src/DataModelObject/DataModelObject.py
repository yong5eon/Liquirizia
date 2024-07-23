# -*- coding: utf-8 -*-

from .DataAttributeObject import DataAttributeObject

from collections.abc import Iterable, Mapping
from copy import copy, deepcopy

__all__ = (
	'DataModelObject'
)


class DataModelObject(Mapping, Iterable):
	"""Abstract Data Model Class of Data Model Object"""

	def __new__(cls, *args, **kwargs):
		o = object.__new__(cls)
		o.__object__ = dict()
		for k, v in cls.__dict__.items():
			if isinstance(v, DataAttributeObject):
				v.__init_object__(o, kwargs[k] if k in kwargs.keys() else None)
		return o

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.__object__.__repr__()[1:-1]
		)

	def __str__(self):
		return self.__object__.__str__()

	# implements interfaces of Iterable
	def __iter__(self):
		return self.__object__.__iter__()

	# implements interfaces of Mapping
	def __getitem__(self, key):
		return self.__object__.__getitem__(key)

	def __len__(self):
		return self.__object__.__len__()

	def __copy__(self):
		return self.__class__.__new__(self.__class__, **self.__object__)

	def __deepcopy__(self, memo={}):
		o = self.__class__.__new__(self.__class__, **self.__object__)
		memo[id(self)] = o
		for k, v in self.__dict__.items():
			setattr(o, k, deepcopy(v, memo))
		return o
