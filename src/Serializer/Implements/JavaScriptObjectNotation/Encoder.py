# -*- coding: utf-8 -*-

from Liquirizia.Serializer import Serializer

from collections.abc import MutableSequence, Sequence, Mapping, Set
from datetime import datetime, date, time
from decimal import Decimal
from json import dumps, JSONEncoder

__all__ = (
	'Encoder'
)


class TypeEncoder(JSONEncoder):
	"""Type Encoder for JSON"""

	def default(self, obj):
		if isinstance(obj, Decimal):
			return float(obj)
		if isinstance(obj, MutableSequence):
			return list(obj)
		if isinstance(obj, Sequence):
			return tuple(obj)
		if isinstance(obj, Set):
			return tuple(obj)
		if isinstance(obj, Mapping):
			return dict(obj)
		if isinstance(obj, (datetime, date, time)):
			return obj.isoformat()
		return None


class Encoder(Serializer):
	"""Encoder Class for JSON"""

	def __call__(self, obj):
		return dumps(
			obj, 
			cls=TypeEncoder,
			ensure_ascii=False, 
		)
	
	
