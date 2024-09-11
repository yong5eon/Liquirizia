# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Context'
)


class Context(metaclass=ABCMeta):
	"""Context Interface for Database"""

	@abstractmethod
	def rows(self):
		raise NotImplementedError('{} must be implemented rows'.format(self.__class__.__name__))

	@abstractmethod
	def row(self):
		raise NotImplementedError('{} must be implemented row'.format(self.__class__.__name__))
	
	@abstractmethod
	def count(self):
		raise NotImplementedError('{} must be implemented count'.format(self.__class__.__name__))

	@property
	@abstractmethod
	def query(self):
		raise NotImplementedError('{} must be implemented query'.format(self.__class__.__name__))