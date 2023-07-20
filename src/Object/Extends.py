# -*- coding: utf-8 -*-

from functools import wraps
from inspect import (
	getmodule,
	getcallargs,
)

__all__ = (
	'Extends',
)


def Extends(fn: callable) -> callable:
	mod = getmodule(fn)
	if '__extends__' not in dir(mod):
		mod.__extends__ = {}
	if fn.__qualname__ not in mod.__extends__:
		mod.__extends__[fn.__qualname__] = []
	if fn not in mod.__extends__[fn.__qualname__]:
		mod.__extends__[fn.__qualname__].append(fn)

	@wraps(fn)
	def f(*args, **kwargs):
		o = None
		for fo in mod.__extends__[fn.__qualname__]:
			try:
				if getcallargs(fo, *args, **kwargs):
					o = fo
					break
			except TypeError as e:
				continue
		if not o:
			raise TypeError('Attempted to call method {} with illegal arguments'.format(fn.__qualname__))
		return o(*args, **kwargs)

	return f
