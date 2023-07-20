# -*- coding: utf-8 -*-

__all__ = (
	'DataAccessObjectConfiguration'
)


class DataAccessObjectConfiguration(object):
	"""
	Data Access Object Configuration Interface
	"""
	def __init__(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))
