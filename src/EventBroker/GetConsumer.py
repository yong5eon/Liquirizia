# -*- coding: utf-8 -*-

from .EventHandler import EventHandler

from abc import ABCMeta, abstractmethod

__all__ = (
	'GetConsumer'
)


class GetConsumer(metaclass=ABCMeta):
	"""GetConsumer Interface for Event Broker"""

	@abstractmethod
	def consumer(self, queue: str, handler: EventHandler = None, **kwargs):
		raise NotImplemented('{} must be implemented consumer'.format(self.__class__.__name__))
