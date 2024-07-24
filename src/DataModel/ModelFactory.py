# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'ModelFactory'
)


class ModelFactory(ABC):
	"""Abstract Model Factory Class with Decorator"""
	@abstractmethod
	def __call__(self, obj):
		pass

	@abstractmethod
	def toString(self):
		pass