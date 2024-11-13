# -*- coding: utf-8 -*-

from .EventHandler import EventHandler

from abc import ABCMeta, abstractmethod

__all__ = (
	'Connection'
)


class Connection(metaclass=ABCMeta):
	"""Connection Interface for Event Broker"""

	@abstractmethod
	def connect(self):
		raise NotImplemented('{} must be implemented connect'.format(self.__class__.__name__))

	@abstractmethod
	def close(self):
		raise NotImplemented('{} must be implemented close'.format(self.__class__.__name__))
