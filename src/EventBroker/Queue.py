# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from .Exchange import Exchange

from typing import Union

__all__ = (
	'Queue'
)


class Queue(metaclass=ABCMeta):
	"""Queue Interface for Event Broker"""

	@abstractmethod
	def __str__(self):
		raise NotImplementedError('{} must be implemented __Str__'.format(self.__class__.__name__))

	@abstractmethod
	def create(self, name: str, **kwargs):
		raise NotImplementedError('{} must be implemented create'.format(self.__class__.__name__))

	@abstractmethod
	def bind(self, exchange: Union[str, Exchange], **kwargs):
		raise NotImplementedError('{} must be implemented bind'.format(self.__class__.__name__))

	@abstractmethod
	def send(self, **kwargs):
		raise NotImplementedError('{} must be implemented send'.format(self.__class__.__name__))

	@abstractmethod
	def unbind(self, exchange: Union[str, Exchange], **kwargs):
		raise NotImplementedError('{} must be implemented unbind'.format(self.__class__.__name__))

	@abstractmethod
	def remove(self):
		raise NotImplementedError('{} must be implemented remove'.format(self.__class__.__name__))
