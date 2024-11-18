# -*- coding: utf-8 -*-

from Liquirizia.DataModel import Model

from abc import ABCMeta, abstractmethod
from typing import Union, Sequence, Mapping, Type


__all__ = (
	'Executor'
)


class Executor(metaclass=ABCMeta):
	"""Executor Interface for Data Model"""

	@abstractmethod
	def __init__(self, o: Type[Model]):
		pass
	
	@property
	@abstractmethod
	def query(self) -> str:
		pass

	@property
	@abstractmethod
	def args(self) -> Union[Sequence, Mapping]:
		pass
	