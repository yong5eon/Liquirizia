# -*- coding: utf-8 -*-

from .EventHandler import EventHandler

from abc import ABCMeta, abstractmethod

__all__ = (
	'Connection',
	'GetExchange',
	'GetQueue',
	'GetConsumer',
)


class Connection(metaclass=ABCMeta):
	"""Connection Interface of Event Broker"""
	@abstractmethod
	def connect(self):
		raise NotImplemented('{} must be implemented connect'.format(self.__class__.__name__))
	@abstractmethod
	def close(self):
		raise NotImplemented('{} must be implemented close'.format(self.__class__.__name__))


class GetExchange(metaclass=ABCMeta):
	"""GetExchange Interface for Connection of Event Broker"""
	@abstractmethod
	def exchange(self, name: str, **kwargs):
		raise NotImplemented('{} must be implemented exchange'.format(self.__class__.__name__))


class GetQueue(metaclass=ABCMeta):
	"""GetQueue Interface for Connection of Event Broker"""
	@abstractmethod
	def queue(self, name: str, **kwargs):
		raise NotImplemented('{} must be implemented queue'.format(self.__class__.__name__))


class GetConsumer(metaclass=ABCMeta):
	"""GetConsumer Interface for Connection of Event Broker"""
	@abstractmethod
	def consumer(self, handler: EventHandler, **kwargs):
		raise NotImplemented('{} must be implemented consumer'.format(self.__class__.__name__))

