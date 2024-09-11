# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Cache'
)


class Cache(metaclass=ABCMeta):
	"""Interface for Cache"""

	@abstractmethod
	def keys(self, key):
		raise NotImplementedError('{} must be implemented keys'.format(self.__class__.__name__))

	@abstractmethod
	def exists(self, key):
		raise NotImplementedError('{} must be implemented exist'.format(self.__class__.__name__))

	@abstractmethod
	def get(self, key):
		raise NotImplementedError('{} must be implemented get'.format(self.__class__.__name__))

	@abstractmethod
	def set(self, key, value, expires=None):
		raise NotImplementedError('{} must be implemented set'.format(self.__class__.__name__))

	@abstractmethod
	def expire(self, key, seconds):
		raise NotImplementedError('{} must be implemented expire'.format(self.__class__.__name__))

	@abstractmethod
	def persist(self, key):
		raise NotImplementedError('{} must be implemented persist'.format(self.__class__.__name__))

	@abstractmethod
	def delete(self, key):
		raise NotImplementedError('{} must be implemented delete'.format(self.__class__.__name__))
