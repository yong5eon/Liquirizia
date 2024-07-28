# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from .Model import Model

__all__ = (
	'ModelExecutor'
)


class ModelExecutor(metaclass=ABCMeta):
	"""Abstract Model Executor Class"""

	@abstractmethod
	def __init__(self, o: type[Model]):
		pass
	
	@abstractmethod
	def __str__(self):
		pass