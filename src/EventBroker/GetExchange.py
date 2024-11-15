# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'GetExchange'
)


class GetExchange(metaclass=ABCMeta):
	"""GetTopic Interface for Event Broker"""

	@abstractmethod
	def exchange(self, name: str = None, **kwargs):
		raise NotImplemented('{} must be implemented exchange'.format(self.__class__.__name__))

