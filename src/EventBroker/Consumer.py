# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Consumer'
)


class Consumer(metaclass=ABCMeta):
	"""Consumer Interface of Event Broker"""
	@abstractmethod
	def subs(self, queue: str):
		raise NotImplementedError('{} must be implemented add'.format(self.__class__.__name__))
	@abstractmethod
	def run(self):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
	@abstractmethod
	def stop(self):
		raise NotImplementedError('{} must be implemented stop'.format(self.__class__.__name__))

