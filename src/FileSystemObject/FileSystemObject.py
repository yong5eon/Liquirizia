# -*- coding: utf-8 -*-

from .FileSystemObjectConfiguration import FileSystemObjectConfiguration

__all__ = (
	'FileSystemObject'
)


class FileSystemObject(object):
	"""
	File System Object Interface
	"""
	def __init__(self, conf: FileSystemObjectConfiguration):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

	def connect(self):
		raise NotImplementedError('{} must be implemented connect'.format(self.__class__.__name__))

	def exist(self, path):
		raise NotImplementedError('{} must be implemented exist'.format(self.__class__.__name__))

	def type(self, path):
		raise NotImplementedError('{} must be implemented type'.format(self.__class__.__name__))

	def timestamp(self, path):
		raise NotImplementedError('{} must be implemented type'.format(self.__class__.__name__))

	def modified(self, path):
		raise NotImplementedError('{} must be implemented type'.format(self.__class__.__name__))

	def etag(self, path):
		raise NotImplementedError('{} must be implemented type'.format(self.__class__.__name__))

	def size(self, path):
		raise NotImplementedError('{} must be implemented type'.format(self.__class__.__name__))

	def open(self, path, *args, **kwargs):
		raise NotImplementedError('{} must be implemented open'.format(self.__class__.__name__))

	def close(self):
		raise NotImplementedError('{} must be implemented close'.format(self.__class__.__name__))

	def files(self, path):
		raise NotImplementedError('{} must be implemented files'.format(self.__class__.__name__))

