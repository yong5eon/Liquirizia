# -*- coding: utf-8 -*-

from .ModelExecutor import ModelExecutor

from abc import abstractmethod
from collections.abc import Iterable

__all__ = (
	'ModelExecutors'
)


class ModelExecutors(ModelExecutor, Iterable):
	"""Abstract Model Executors Class"""

	@abstractmethod
	def __iter__(self):
		pass