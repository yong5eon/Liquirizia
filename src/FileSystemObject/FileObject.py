# -*- coding: utf-8 -*-

from .FileSystemObject import FileSystemObject

__all__ = (
	'FileObject'
)


class FileObject(object):
	"""
	File Object Interface
	"""
	def __init__(self, fso: FileSystemObject):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

	def __enter__(self):
		raise NotImplementedError('{} must be implemented __enter__'.format(self.__class__.__name__))

	def __exit__(self, exc_type, exc_val, exc_tb):
		raise NotImplementedError('{} must be implemented __exit__'.format(self.__class__.__name__))

	def open(self, path, *args, **kwargs):
		raise NotImplementedError('{} must be implemented open'.format(self.__class__.__name__))

	def read(self, size=None):
		raise NotImplementedError('{} must be implemented read'.format(self.__class__.__name__))

	def write(self, buffer):
		raise NotImplementedError('{} must be implemented write'.format(self.__class__.__name__))

	def close(self):
		raise NotImplementedError('{} must be implemented close'.format(self.__class__.__name__))
