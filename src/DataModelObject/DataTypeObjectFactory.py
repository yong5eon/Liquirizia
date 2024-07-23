# -*- coding: utf-8 -*-

from .DataTypeObject import DataTypeObject

__all__ = (
	'DataTypeObjectFactory'
)


class DataTypeObjectFactory(DataTypeObject):
	"""Data Type Object Factory"""
	@classmethod
	def __new__(cls, *args, **kwargs):
		v = args[1]
		o = args[2]
		m = args[3]
		if isinstance(v, int):
			from .Types import Integer
			return Integer(v, o, m)
		if isinstance(v, float):
			from .Types import Float
			return Float(v, o, m)
		if isinstance(v, str):
			from .Types import String
			return String(v, o, m)
		if isinstance(v, tuple):
			from .Types import Tuple
			return Tuple(v, o, m)
		if isinstance(v, list):
			from .Types import List
			return List(v, o, m)
		if isinstance(v, dict):
			from .Types import Dictionary
			return Dictionary(v, o, m)
		from .Types import Object
		return Object(v, o, m)

