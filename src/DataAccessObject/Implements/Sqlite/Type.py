# -*- coding: utf-8 -*-

from Liquirizia.DataModel import Value, MISSING, Handler
from Liquirizia.Validator.Validator import Validator

from abc import ABCMeta

from typing import Any, Sequence

__all__ = (
	'Type'
)


class TypeCreateor(ABCMeta):
    def __repr__(cls): return cls.typestr


class Type(Value, metaclass=TypeCreateor):
	def __init__(
		self, 
		key : str,
		type: str,
		va: Validator = None,
		fn: Handler = None,
		null: bool = False,
		default: Any = None,
		description: str = None,
	):
		super().__init__(
			type=type,
			va=va,
			fn=fn,
			default=None if null else MISSING,
			description=description,
		)
		self.key = key
		self.null = null
		self.coldef = default
		return
	
	def __init_subclass__(cls, typestr: str = None):
		cls.typestr = typestr
		return
	
	def __str__(self):
		return '{}.{}'.format(
			self.model.__model__,
			self.key
		)

	def encode(self, o: any): return o	

	@classmethod
	def ToTypeString(cls): return cls.typestr
