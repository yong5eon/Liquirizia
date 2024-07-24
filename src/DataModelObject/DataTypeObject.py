# -*- coding: utf-8 -*-

from abc import ABC
from operator import *

__all__ = (
	'DataTypeObject'
)


class DataTypeObject(ABC):
	"""Abstract Data Type Object Class of Data Model Object"""
	def __new__(
		cls,
		value,
		attr,
		model,
	):
		n = object.__new__(cls)
		n.__value__= value
		n.__attr__ = attr
		n.__model__ = model
		return n

	def __repr__(self):
		return self.__value__.__repr__()
	
	def __str__(self):
		return self.__value__.__str__()
