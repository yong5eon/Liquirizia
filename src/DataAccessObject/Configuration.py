# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Configuration'
)


class Configuration(metaclass=ABCMeta):
	"""Configuration Interface"""

	@abstractmethod
	def __init__(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))
