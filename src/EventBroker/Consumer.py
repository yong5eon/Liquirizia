# -*- coding: utf-8 -*-

from .Event import Event

from abc import ABCMeta, abstractmethod

__all__ = (
	'Consumer'
)


class Consumer(metaclass=ABCMeta):
	"""Consumer Interface of Event Broker"""

	@abstractmethod
	def qos(self, **kwargs):
		raise NotImplementedError('{} must be implemented qos'.format(self.__class__.__name__))
	
	def read(self, **kwargs) -> Event:
		raise NotImplementedError('{} must be implemented read'.format(self.__class__.__name__))

	@abstractmethod
	def run(self, **kwargs):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))

	@abstractmethod
	def stop(self):
		raise NotImplementedError('{} must be implemented stop'.format(self.__class__.__name__))
