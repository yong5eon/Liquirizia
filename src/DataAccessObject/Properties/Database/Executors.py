# -*- coding: utf-8 -*-

from Liquirizia.DataModel import Model

from .Executor import Executor

from abc import abstractmethod
from collections.abc import Iterable

from typing import Type, Iterable

__all__ = (
	'Executors'
)


class Executors(Iterable):
	"""Executors Interface for Data Model"""

	@abstractmethod
	def __init__(self, o: Type[Model]):
		pass
	
	@abstractmethod
	def __iter__(self) -> Iterable[Executor]:
		pass

