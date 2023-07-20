# -*- coding: utf-8 -*-

from functools import wraps
from sys import _getframe as getframe

__all__ = (
	'Private',
)


def Private(fn: callable) -> callable:
	qualname = getframe(1).f_locals.get('__qualname__', None)
	@wraps(fn)
	def f(self, *args, **kwargs):
		caller = getframe(1)
		code = caller.f_code
		name = code.co_name
		while name[0] == '<' and name[len(name)-1] == '>' and caller.f_back:
			caller = caller.f_back
			code = caller.f_code
			name = code.co_name
		c = self.__class__
		cs = [co for co in c.mro() if name in co.__dict__]
		for co in cs:
			call = co.__dict__[name]
			call = call.__dict__['__wrapped__'] if '__wrapper__' in call.__dict__ else call
			if call.__code__ == code and qualname == co.__qualname__ and qualname == c.__name__:
				return fn(self, *args, **kwargs)
		raise RuntimeError('Attempted call to private method {}'.format(fn))
	return f
