# -*- coding: utf-8 -*-

from abc import (
	ABC,
	ABCMeta,
	abstractmethod
)

__all__ = (
	'Singleton'
)


class Meta(ABCMeta):
	"""Singleton Meta Class"""
	def __call__(cls, *args, **kwargs):
		try:
			o = getattr(cls, '__object__')
			if len(args) or len(kwargs.items()):
				raise RuntimeError('{} is singleton, it is already initialized'.format(cls.__name__))
			return o
		except AttributeError:
			cls.__object__ = super().__call__(*args, **kwargs)
			return cls.__object__


class Singleton(ABC, metaclass=Meta):
	"""Singleton Base Class"""
	def __copy__(self): return self
	def __deepcopy__(self, memodict={}): return self
