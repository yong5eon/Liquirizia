# -*- coding: utf-8 -*-

__all__ = (
	'Configuration'
)


class Configuration(object):
	"""
	Configuration Interface for Event Broker
	"""
	def __init__(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))
