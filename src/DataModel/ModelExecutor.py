# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from collections.abc import Iterable

from .Model import Model

__all__ = (
	'ModelExecutor'
)


class ModelExecutor(ABC):
	"""Abstract Model Executor Class"""

	@abstractmethod
	def __init__(self, o: type[Model]):
		pass
	
	@abstractmethod
	def __iter__(self):
		pass