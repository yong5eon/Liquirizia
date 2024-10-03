# -*- coding: utf-8 -*-

from .Connection import Connection

from abc import ABCMeta, abstractmethod

__all__ = (
	'File'
)


class File(metaclass=ABCMeta):
	"""File Interface"""

	@abstractmethod
	def __init__(self, fso: Connection):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

	@abstractmethod
	def __enter__(self):
		raise NotImplementedError('{} must be implemented __enter__'.format(self.__class__.__name__))

	@abstractmethod
	def __exit__(self, exc_type, exc_val, exc_tb):
		raise NotImplementedError('{} must be implemented __exit__'.format(self.__class__.__name__))

	@abstractmethod
	def open(self, path, *args, **kwargs):
		raise NotImplementedError('{} must be implemented open'.format(self.__class__.__name__))

	@abstractmethod
	def read(self, size=None):
		raise NotImplementedError('{} must be implemented read'.format(self.__class__.__name__))

	@abstractmethod
	def write(self, buffer):
		raise NotImplementedError('{} must be implemented write'.format(self.__class__.__name__))

	@abstractmethod
	def close(self):
		raise NotImplementedError('{} must be implemented close'.format(self.__class__.__name__))
