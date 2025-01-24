# -*- coding: utf-8 -*-

from ...Serializer import Serializer
from ...Errors import DecodeError

from json import loads, JSONDecoder
from datetime import date, datetime
from re import compile

__all__ = (
	'Decoder'
)

REGEX_DATETIME_ISO_FORMAT = compile(
	r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?$'
)
REGEX_DATE_ISO_FORMAT = compile(
	r'^\d{4}-\d{2}-\d{2}$'
)

class TypeDecoder(JSONDecoder):
	"""Type Decoder for JSON"""
	
	def __init__(self, *args, **kwargs):
		super(TypeDecoder, self).__init__(object_hook=self.any, *args, **kwargs)
		return
	
	def any(self, obj):
		if isinstance(obj, dict):
			for key, value in obj.items():
				if isinstance(value, str):
					try:
						if REGEX_DATE_ISO_FORMAT.match(value):
							obj[key] = date.fromisoformat(value)
						continue
					except:
						pass
					try:
						if REGEX_DATETIME_ISO_FORMAT.match(value):
							obj[key] = datetime.fromisoformat(value)
						continue
					except:
						pass
				elif isinstance(value, (list, tuple)):
					for i, v in enumerate(value):
						if isinstance(v, str):
							try:
								if REGEX_DATETIME_ISO_FORMAT.match(v):
									value[i] = date.fromisoformat(v)
								continue
							except:
								pass
							try:
								if REGEX_DATETIME_ISO_FORMAT.match(v):
									value[i] = datetime.fromisoformat(v)
								continue
							except:
								pass
		return obj


class Decoder(Serializer):
	"""Decoder Class for JSON"""
	
	def __call__(self, obj):
		if not isinstance(obj, str):
			raise DecodeError('{} is not string'.format(obj))
		try:
			return loads(obj, cls=TypeDecoder)
		except Exception as e:
			raise DecodeError(str(e), error=e)
