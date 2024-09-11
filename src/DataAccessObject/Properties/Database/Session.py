# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Session'
)


class Session(metaclass=ABCMeta):
	"""Session Interface for Database"""

	@abstractmethod
	def execute(self, sql, *args, **kwargs):
		raise NotImplementedError('{} must be implemented execute'.format(self.__class__.__name__))

	@abstractmethod
	def executes(self, sql, *args, **kwargs):
		raise NotImplementedError('{} must be implemented execute'.format(self.__class__.__name__))

	@abstractmethod
	def rows(self):
		raise NotImplementedError('{} must be implemented rows'.format(self.__class__.__name__))
	
	@abstractmethod
	def row(self):
		raise NotImplementedError('{} must be implemented row'.format(self.__class__.__name__))

	@abstractmethod
	def count(self):
		raise NotImplementedError('{} must be implemented count'.format(self.__class__.__name__))