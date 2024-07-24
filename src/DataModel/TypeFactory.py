# -*- coding: utf-8 -*-

from .Type import Type

__all__ = (
	'TypeFactory'
)


class TypeFactory(Type):
	"""Type Factory"""
	@classmethod
	def __new__(cls, *args, **kwargs):
		value = args[1]
		attr = args[2]
		model = args[3]
		if isinstance(value, int):
			from .Types import Integer
			return Integer(value, attr, model)
		if isinstance(value, float):
			from .Types import Float
			return Float(value, attr, model)
		if isinstance(value, str):
			from .Types import String
			return String(value, attr, model)
		if isinstance(value, tuple):
			from .Types import Tuple
			return Tuple(value, attr, model)
		if isinstance(value, list):
			from .Types import List
			return List(value, attr, model)
		if isinstance(value, dict):
			from .Types import Dictionary
			return Dictionary(value, attr, model)
		from .Types import Object
		return Object(value, attr, model)

