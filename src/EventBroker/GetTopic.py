# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'GetTopic'
)


class GetTopic(metaclass=ABCMeta):
	"""GetTopic Interface for Event Broker"""

	@abstractmethod
	def topic(self, topic: str = None, **kwargs):
		raise NotImplemented('{} must be implemented topic'.format(self.__class__.__name__))

