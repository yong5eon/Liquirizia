# -*- coding: utf-8 -*-

from .Configuration import Configuration

from abc import ABCMeta, abstractmethod

__all__ = (
	'Connection'
)


class Connection(metaclass=ABCMeta):
	"""File System Object Interface"""

	@abstractmethod
	def __init__(self, conf: Configuration):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

	@abstractmethod
	def connect(self):
		raise NotImplementedError('{} must be implemented connect'.format(self.__class__.__name__))

	@abstractmethod
	def exist(self, path):
		raise NotImplementedError('{} must be implemented exist'.format(self.__class__.__name__))

	@abstractmethod
	def type(self, path):
		raise NotImplementedError('{} must be implemented type'.format(self.__class__.__name__))

	@abstractmethod
	def timestamp(self, path):
		raise NotImplementedError('{} must be implemented type'.format(self.__class__.__name__))

	@abstractmethod
	def modified(self, path):
		raise NotImplementedError('{} must be implemented type'.format(self.__class__.__name__))

	@abstractmethod
	def etag(self, path):
		raise NotImplementedError('{} must be implemented type'.format(self.__class__.__name__))

	@abstractmethod
	def size(self, path):
		raise NotImplementedError('{} must be implemented type'.format(self.__class__.__name__))

	@abstractmethod
	def open(self, path, *args, **kwargs):
		raise NotImplementedError('{} must be implemented open'.format(self.__class__.__name__))

	@abstractmethod
	def close(self):
		raise NotImplementedError('{} must be implemented close'.format(self.__class__.__name__))

	@abstractmethod
	def files(self, path):
		raise NotImplementedError('{} must be implemented files'.format(self.__class__.__name__))
