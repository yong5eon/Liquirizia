# -*- coding: utf-8 -*-

from .Configuration import Configuration

from abc import ABCMeta, abstractmethod

__all__ = (
	'Connection'
)


class Connection(metaclass=ABCMeta):
	"""Connection Interface"""

	@abstractmethod
	def __init__(self, conf: Configuration):
		raise NotImplementedError('{} must be implemented __init__ method'.format(self.__class__.__name__))

	@abstractmethod
	def connect(self):
		raise NotImplementedError('{} must be implemented connect method'.format(self.__class__.__name__))

	@abstractmethod
	def close(self):
		raise NotImplementedError('{} must be implemented close method'.format(self.__class__.__name__))
