# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from typing import Optional

__all__ = (
	'Queue',
	'Gettable',
	'Readable',
)


class Queue(metaclass=ABCMeta):
	"""Queue Interface for Event Broker"""
	@abstractmethod
	def send(self, **kwargs):
		raise NotImplementedError('{} must be implemented send'.format(self.__class__.__name__))


class Gettable(metaclass=ABCMeta):
	"""Gettable Interface for Queue of Event Broker"""
	@abstractmethod
	def get(self, timeout: int = None):
		raise NotImplementedError('{} must be implemented get'.format(self.__class__.__name__))


class Readable(metaclass=ABCMeta):
	"""Readable Interface for Queue of Event Broker"""
	@abstractmethod
	def read(self, timeout: int = None):
		raise NotImplementedError('{} must be implemented read'.format(self.__class__.__name__))

