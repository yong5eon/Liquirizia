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
	"""
	Singleton Meta Class
	"""

	__object__ = {}

	def __call__(cls, *args, **kwargs):
		if cls.__object__ and (len(args) or len(kwargs.items())):
			raise RuntimeError('{} is singleton, it is already initialized'.format(cls.__name__))
		if cls not in cls.__object__:
			cls.__object__[cls] = super(Meta, cls).__call__(*args, **kwargs)
		return cls.__object__[cls]


class Singleton(ABC, metaclass=Meta):
	"""
	Singleton Base Class
	"""
	pass
