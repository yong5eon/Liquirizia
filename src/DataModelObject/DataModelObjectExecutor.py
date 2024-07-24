# -*- coding: utf-8 -*-

from .DataModelObject import DataModelObject

from abc import ABC, ABCMeta, abstractmethod

__all__ = (
	'DataModelObjectExecutor'
)


class DataModelObjectExecutor(ABC):
	"""Abstract Data Model Object Executor Class"""

	def __init__(self, o: type[DataModelObject]):
		super().__init__()
		self.model = o
		return