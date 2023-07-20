# -*- coding: utf-8 -*-

from inspect import (
	getmembers,
	isfunction,
	ismethod,
)
from types import MethodType

__all__ = (
	'Implements',
)


def Implements(*args):
	def decorator(obj: type) -> type:
		exists = [name for name, f in getmembers(obj, predicate=isfunction)]
		for i in args:
			methods = getmembers(i, predicate=ismethod)
			for m in methods:
				if m[0] not in exists:
					method = MethodType(m[1], obj)
					setattr(obj, m[0], method)
		return obj
	return decorator
