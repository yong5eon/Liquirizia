# -*- coding: utf-8 -*-

from Liquirizia.Serializer import Serializer

from json import loads, JSONDecoder
from datetime import datetime, date, time

from collections.abc import Sequence, Mapping

from typing import Any

__all__ = (
	'Decoder'
)


class TypeDecoder(JSONDecoder):
	"""Type Decoder for JSON"""
	
	def __init__(self, *args, **kwargs):
		super(TypeDecoder, self).__init__(object_hook=self.any, *args, **kwargs)
		return
	
	def string(self, obj: str):
		try:
			return time.fromisoformat(obj)
		except:
			pass
		try:
			return date.fromisoformat(obj)
		except:
			pass
		try:
			return datetime.fromisoformat(obj)
		except:
			pass
		return obj
	
	def object(self, obj: Mapping):
		for key, value in obj.items():
			if isinstance(value, str):
				value = self.string(value)
				continue
			if isinstance(value, Sequence):
				value = self.array(value)
				continue
			if isinstance(value, Mapping):
				value = self.object(value)
				continue
		return obj
	
	def array(self, obj: Sequence):
		for value in obj:
			if isinstance(value, str):
				value = self.string(value)
				continue
			if isinstance(value, Sequence):
				value = self.array(value)
				continue
			if isinstance(value, Mapping):
				value = self.array(value)
				continue
		return obj
	
	def any(self, obj: Any):
		if isinstance(obj, str): return self.string(obj)
		if isinstance(obj, Mapping): return self.object(obj)
		if isinstance(obj, Sequence): return self.array(obj)
		return obj
	

class Decoder(Serializer):
	"""Decoder Class for JSON"""
	
	def __call__(self, obj):
		if not isinstance(obj, str):
			raise RuntimeError('{} is not string'.format(obj))
		return loads(
			obj,
			cls=TypeDecoder,
		)
	
	
