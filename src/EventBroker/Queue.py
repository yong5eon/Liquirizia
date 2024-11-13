# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Queue'
)


class Queue(metaclass=ABCMeta):
	"""Queue Interface for Event Broker"""

	@abstractmethod
	def create(self, queue, **kwargs):
		raise NotImplementedError('{} must be implemented declare'.format(self.__class__.__name__))

	@abstractmethod
	def bind(self, topic, **kwargs):
		raise NotImplementedError('{} must be implemented bind'.format(self.__class__.__name__))

	@abstractmethod
	def send(self, **kwargs):
		raise NotImplementedError('{} must be implemented send'.format(self.__class__.__name__))

	@abstractmethod
	def unbind(self, topic, **kwargs):
		raise NotImplementedError('{} must be implemented unbind'.format(self.__class__.__name__))

	@abstractmethod
	def remove(self):
		raise NotImplementedError('{} must be implemented remove'.format(self.__class__.__name__))
