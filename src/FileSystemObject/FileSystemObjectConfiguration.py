# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'FileSystemObjectConfiguration'
)


class FileSystemObjectConfiguration(ABC):
	"""File System Object Configuration Interface"""

	@abstractmethod
	def __init__(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))
