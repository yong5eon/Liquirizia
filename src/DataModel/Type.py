# -*- coding: utf-8 -*-

from abc import ABC
from operator import *
from collections.abc import Sequence, Mapping

__all__ = (
	'Type'
)


class Type(ABC):
	"""Abstract Type Class of Data Model"""

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
	
	@classmethod
	def Create(cls, value, attr, model):
		PATTERNS = [type(None), bool, int, float, str, bytes]
		if type(value) in PATTERNS:
			return value
		if isinstance(value, Sequence):
			from .Types import List
			return List(value, attr, model)
		if isinstance(value, Mapping):
			from .Types import Dictionary
			return Dictionary(value, attr, model)
		from .Types import Object
		return Object(value, attr, model)
