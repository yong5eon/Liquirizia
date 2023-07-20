# -*- coding: utf-8 -*-

from .DataAccessObject import DataAccessObject

__all__ = (
	'DataTypeObject'
)


class DataTypeObject(object):
	"""
	Data Type Object Interface Class
	"""
	def __init__(self, obj: DataAccessObject):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

