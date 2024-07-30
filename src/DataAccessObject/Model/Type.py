# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Type',
)


class Type(metaclass=ABCMeta):
	"""Type Interface for Data Model to use as a Decorator"""

	@abstractmethod
	def __call__(self, obj):
		pass
