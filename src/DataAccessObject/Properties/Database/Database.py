# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Database'
)


class Database(metaclass=ABCMeta):
	"""Interface for Database"""

	@abstractmethod
	def begin(self):
		raise NotImplementedError('{} must be implemented begin'.format(self.__class__.__name__))

	@abstractmethod
	def execute(self, sql, *args, **kwargs):
		raise NotImplementedError('{} must be implemented execute'.format(self.__class__.__name__))

	@abstractmethod
	def affected(self):
		raise NotImplementedError('{} must be implemented affected'.format(self.__class__.__name__))

	@abstractmethod
	def rows(self):
		raise NotImplementedError('{} must be implemented rows'.format(self.__class__.__name__))

	@abstractmethod
	def commit(self):
		raise NotImplementedError('{} must be implemented commit'.format(self.__class__.__name__))

	@abstractmethod
	def rollback(self):
		raise NotImplementedError('{} must be implemented rollback'.format(self.__class__.__name__))
