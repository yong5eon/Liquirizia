# -*- coding: utf-8 -*-

from .Callback import Callback

__all__ = (
	'Connection'
)


class Connection(object):
	"""
	Connection Interface for Event Broker
	"""
	def connect(self):
		raise NotImplemented('{} must be implemented connect'.format(self.__class__.__name__))

	def topic(self, topic: str = None):
		raise NotImplemented('{} must be implemented topic'.format(self.__class__.__name__))

	def queue(self, queue: str = None):
		raise NotImplemented('{} must be implemented queue'.format(self.__class__.__name__))

	def consumer(self, callback: Callback, count: int = 1):
		raise NotImplemented('{} must be implemented consumer'.format(self.__class__.__name__))

	def close(self):
		raise NotImplemented('{} must be implemented close'.format(self.__class__.__name__))
