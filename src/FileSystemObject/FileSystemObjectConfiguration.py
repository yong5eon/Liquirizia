# -*- coding: utf-8 -*-

__all__ = (
	'FileSystemObjectConfiguration'
)


class FileSystemObjectConfiguration(object):
	"""
	File System Object Configuration Interface
	"""
	def __init__(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))
