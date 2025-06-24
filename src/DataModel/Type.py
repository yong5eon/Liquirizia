# -*- coding: utf-8 -*-

from abc import ABC
from typing import Any

__all__ = (
	'Type'
)


class Type(ABC):
	"""Abstract Type Class of Data Model"""

	def __init__(
		self,
		v: Any,
		obj,
		descriptor,
	):
		self.__value__ = v
		self.__model__ = obj
		self.__descriptor__ = descriptor
		return
	
	def __repr__(self):
		return self.__value__.__repr__()

	@classmethod
	def Create(cls, v: Any, obj, descriptor):
		from .Model import Model
		from dataclasses import is_dataclass
		from decimal import Decimal
		from datetime import datetime, date, time
		if isinstance(v, Model):
			from .Types import DataModel
			return DataModel(v, obj, descriptor)
		if is_dataclass(v):
			from .Types import DataObject
			return DataObject(v, obj, descriptor)
		if isinstance(v, tuple):
			from .Types import Tuple
			return Tuple(v, obj, descriptor)
		if isinstance(v, set):
			from .Types import Set
			return Set(v, obj, descriptor)
		if isinstance(v, list):
			from .Types import List
			return List(v, obj, descriptor)
		if isinstance(v, dict):
			from .Types import Object
			return Object(v, obj, descriptor)
		if isinstance(v, bytearray):
			from .Types import ByteArray
			return ByteArray(v, obj, descriptor)
		PATTERNS = [
			type(None),
			bool,
			int,
			float,
			str,
			bytes,
			Decimal,
			datetime,
			date,
			time,
		]
		if type(v) in PATTERNS:
			return v
		raise TypeError(
			'Not supported type {} for value {}'.format(
				type(v),
				v
			)
		)
