# -*- coding: utf-8 -*-

from .Model import Model

from abc import ABC, ABCMeta, abstractmethod

__all__ = (
	'ModelExecutor'
)


class ModelExecutor(ABC):
	"""Abstract Model Executor Class"""

	def __init__(self, o: type[Model]):
		super().__init__()
		self.model = o
		return