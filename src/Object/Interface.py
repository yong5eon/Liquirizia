# -*- coding: utf-8 -*-

from inspect import (
	getfullargspec,
	getmembers,
	isfunction,
)

from types import MethodType

__all__ = (
	'Interface',
)


def Interface(obj: type) -> type:
	CODE = 'def {}(*args, **kwargs):\n raise NotImplementedError("{} must be implemented")'
	li = getmembers(obj, predicate=isfunction)
	for i in li:
		spec = getfullargspec(i[1])
		code = CODE.format(i[0], i[0])
		compiled = compile(code, '<string>', 'exec')
		exec(compiled)
		m = MethodType(locals()[i[0]], obj)
		setattr(obj, i[0], m)
	return obj
