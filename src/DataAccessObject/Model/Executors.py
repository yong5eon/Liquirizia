# -*- coding: utf-8 -*-

from ...DataModel import Model

from abc import abstractmethod
from collections.abc import Iterable

__all__ = (
	'Executors'
)


class Executors(Iterable):
	"""Executors Interface for Data Model"""

	@abstractmethod
	def __init__(self, o: type[Model]):
		pass
	
	@abstractmethod
	def __iter__(self):
		pass