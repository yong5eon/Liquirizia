# -*- coding: utf-8 -*-

from ..Pattern import Pattern

from ...Response import Response

from ast import literal_eval

__all__ = (
	'TypeEvaluate'
)


class TypeEvaluate(Pattern):
	def __init__(self):
		return

	def __call__(self, parameter) -> (any, (Response, None)):
		if not isinstance(parameter, str):
			return parameter, None
		try:
			return literal_eval(parameter), None
		except:
			return None, None
