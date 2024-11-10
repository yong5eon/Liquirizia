# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Consumer'
)


class Consumer(metaclass=ABCMeta):
	"""Consumer Interface of Event Broker"""

	@abstractmethod
	def qos(self, **kwargs):
		raise NotImplementedError('{} must be implemented qos'.format(self.__class__.__name__))

	@abstractmethod
	def consume(self, queue: str):
		raise NotImplementedError('{} must be implemented consume'.format(self.__class__.__name__))

	@abstractmethod
	def run(self, **kwargs):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))

	@abstractmethod
	def stop(self):
		raise NotImplementedError('{} must be implemented stop'.format(self.__class__.__name__))
