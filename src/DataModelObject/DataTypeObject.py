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
		v,
		o,
		m,
	):
		n = object.__new__(cls)
		n.__value__= v
		n.__object__ = o
		n.__model__ = m
		return n

	def __repr__(self):
		return self.__value__.__repr__()
	
	def __str__(self):
		return self.__value__.__str__()
