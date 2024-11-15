# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'GetQueue'
)


class GetQueue(metaclass=ABCMeta):
	"""GetQueue Interface for Event Broker"""

	@abstractmethod
	def queue(self, name: str = None, **kwargs):
		raise NotImplemented('{} must be implemented queue'.format(self.__class__.__name__))
