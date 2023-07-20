# -*- coding: utf-8 -*-

from functools import wraps
from sys import _getframe as getframe

__all__ = (
	'Protected',
)


def Protected(fn: callable) -> callable:
	@wraps(fn)
	def f(self, *args, **kwargs):
		caller = getframe(1)
		instance = caller.f_locals.get('self')
		if instance is not self:
			raise RuntimeError('Attempted call to protected method {}'.format(fn))
		return fn(self, *args, **kwargs)
	return f
