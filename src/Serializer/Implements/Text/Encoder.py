# -*- coding: utf-8 -*-

from Liquirizia.Serializer import Serializer

from collections.abc import MutableSequence, Sequence, Set, Mapping
from datetime import datetime, date, time

__all__ = (
	'Encoder'
)


class Encoder(Serializer):
	"""Encoder Class for Text"""

	def __call__(self, obj):
		if isinstance(obj, str): return str(obj)
		if isinstance(obj, datetime): return obj.isoformat()
		if isinstance(obj, date): return obj.isoformat()
		if isinstance(obj, time): return obj.isoformat()
		# TODO : each elements to string
		if isinstance(obj, MutableSequence): return str(list(obj))
		if isinstance(obj, Sequence): return str(tuple(obj))
		if isinstance(obj, Set): return str(set(obj))
		if isinstance(obj, Mapping): return str(dict(obj))
		return str(obj)
