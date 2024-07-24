# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod, abstractclassmethod

__all__ = (
	'DataModelObjectFactory'
)


class DataModelObjectFactory(ABC):
	"""Abstract Data Model Object Factory Class using Decorator"""
	@abstractmethod
	def __call__(self, obj):
		pass

	@abstractmethod
	def toString(self):
		pass