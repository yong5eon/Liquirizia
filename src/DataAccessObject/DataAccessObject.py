# -*- coding: utf-8 -*-

from .DataAccessObjectConfiguration import DataAccessObjectConfiguration

__all__ = (
	'DataAccessObject'
)


class DataAccessObject(object):
	"""
	Data Access Object Interface
	"""

	def __init__(self, conf: DataAccessObjectConfiguration):
		raise NotImplementedError('{} must be implemented __init__ method'.format(self.__class__.__name__))

	def connect(self):
		raise NotImplementedError('{} must be implemented connect method'.format(self.__class__.__name__))

	def close(self):
		raise NotImplementedError('{} must be implemented close method'.format(self.__class__.__name__))
