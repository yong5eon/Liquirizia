# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Formatter'
)

class Formatter(metaclass=ABCMeta):
	"""Log Formatter Interface"""
	@abstractmethod
	def __call__(self, record) -> str:
		raise NotImplemented('{} must be implemented __call__'.format(self.__class__.__name__))
