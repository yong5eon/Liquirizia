# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Event'
)


class Event(metaclass=ABCMeta):
	"""Event Interface of Event Broker"""

	@abstractmethod
	def ack(self):
		raise NotImplementedError('{} must be implemented ack'.format(self.__class__.__name__))

	@abstractmethod
	def nack(self):
		raise NotImplementedError('{} must be implemented nack'.format(self.__class__.__name__))

	@abstractmethod
	def reject(self):
		raise NotImplementedError('{} must be implemented reject'.format(self.__class__.__name__))

	@abstractmethod
	def headers(self):
		raise NotImplementedError('{} must be implemented headers'.format(self.__class__.__name__))

	@abstractmethod
	def header(self, key):
		raise NotImplementedError('{} must be implemented header'.format(self.__class__.__name__))

	@property
	@abstractmethod
	def src(self):
		raise NotImplementedError('{} must be implemented src'.format(self.__class__.__name__))

	@property
	@abstractmethod
	def id(self):
		raise NotImplementedError('{} must be implemented id'.format(self.__class__.__name__))

	@property
	@abstractmethod
	def type(self):
		raise NotImplementedError('{} must be implemented event'.format(self.__class__.__name__))

	@property
	@abstractmethod
	def format(self):
		raise NotImplementedError('{} must be implemented event'.format(self.__class__.__name__))

	@property
	@abstractmethod
	def charset(self):
		raise NotImplementedError('{} must be implemented event'.format(self.__class__.__name__))

	@property
	@abstractmethod
	def body(self):
		raise NotImplementedError('{} must be implemented body'.format(self.__class__.__name__))
