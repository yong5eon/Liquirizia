# -*- coding: utf-8 -*-

from .Connection import Connection

from abc import ABCMeta, abstractmethod

__all__ = (
	'Type'
)


class Type(metaclass=ABCMeta):
	"""Type Interface"""

	@abstractmethod
	def __init__(self, con: Connection):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

