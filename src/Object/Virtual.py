# -*- coding: utf-8 -*-

__all__ = (
	'Private',
	'Protected',
	'Virtual',
	'Extends',
	'Interface',
	'Implements',
)


def Virtual(fn: callable) -> callable:
	def f(*args, **kwargs):
		raise NotImplementedError('{} must be implemented'.format(fn.__name__))
	return f
