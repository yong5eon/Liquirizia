# -*- coding: utf-8 -*-

from Liquirizia.Serializer import Serializer

from ast import literal_eval

__all__ = (
	'Decoder'
)


class Decoder(Serializer):
	"""Decoder Class for Text"""

	def __call__(self, obj):
		if not isinstance(obj, str):
			raise RuntimeError('{} is not string'.format(obj))
		try:
			obj = literal_eval(obj)
			if isinstance(obj, str):
				# TODO : decode string to specialized types
				pass
			return obj
		except:
			return obj
