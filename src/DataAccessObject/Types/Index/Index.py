# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Index'
)


class Index(metaclass=ABCMeta):
	"""Interface for Index"""

	@abstractmethod
	def create(self, index, *args, **kwargs):
		raise NotImplementedError('{} must be implemented create'.format(self.__class__.__name__))

	@abstractmethod
	def delete(self, index):
		raise NotImplementedError('{} must be implemented delete'.format(self.__class__.__name__))

	@abstractmethod
	def total(self, index):
		raise NotImplementedError('{} must be implemented count'.format(self.__class__.__name__))

	@abstractmethod
	def set(self, index, *args, **kwargs):
		raise NotImplementedError('{} must be implemented set'.format(self.__class__.__name__))

	@abstractmethod
	def get(self, index, id):
		raise NotImplementedError('{} must be implemented get'.format(self.__class__.__name__))

	@abstractmethod
	def exists(self, index, id):
		raise NotImplementedError('{} must be implemented exists'.format(self.__class__.__name__))

	@abstractmethod
	def count(self, index, *args, **kwargs):
		raise NotImplementedError('{} must be implemented search'.format(self.__class__.__name__))

	@abstractmethod
	def query(self, index, *args, **kwargs):
		raise NotImplementedError('{} must be implemented search'.format(self.__class__.__name__))
