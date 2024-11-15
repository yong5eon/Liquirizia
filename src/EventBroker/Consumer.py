# -*- coding: utf-8 -*-

from .Event import Event

from abc import ABCMeta, abstractmethod

from typing import Optional

__all__ = (
	'Consumer'
)


class Consumer(metaclass=ABCMeta):
	"""Consumer Interface of Event Broker"""

	@abstractmethod
	def read(self, timeout: float = None) -> Optional[Event]:
		raise NotImplementedError('{} must be implemented read'.format(self.__class__.__name__))

	@abstractmethod
	def run(self):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))

	@abstractmethod
	def stop(self):
		raise NotImplementedError('{} must be implemented stop'.format(self.__class__.__name__))
