# -*- coding: utf-8 -*-

from .Context import Context
from .Cursor import Cursor
from .Session import Session

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
	def execute(self, sql, *args, **kwargs) -> Context:
		raise NotImplementedError('{} must be implemented execute'.format(self.__class__.__name__))

	@abstractmethod
	def executes(self, sql, *args, **kwargs) -> Context:
		raise NotImplementedError('{} must be implemented executes'.format(self.__class__.__name__))
	
	@abstractmethod
	def cursor(self) -> Cursor:
		raise NotImplementedError('{} must be implemented Cursor'.format(self.__class__.__name__))
	
	@abstractmethod
	def session(self) -> Session:
		raise NotImplementedError('{} must be implemented session'.format(self.__class__.__name__))

	@abstractmethod
	def commit(self):
		raise NotImplementedError('{} must be implemented commit'.format(self.__class__.__name__))

	@abstractmethod
	def rollback(self):
		raise NotImplementedError('{} must be implemented rollback'.format(self.__class__.__name__))