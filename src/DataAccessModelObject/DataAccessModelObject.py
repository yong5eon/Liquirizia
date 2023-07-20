# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import DataAccessObject

__all__ = (
	'DataAccessModelObject'
)


class DataAccessModelObject(object):
	"""
	Data Access Model Object Interface
	"""
	def __init__(self, connection: DataAccessObject):
		raise NotImplementedError('{} must be implemented __init__ method'.format(self.__class__.__name__))
