# -*- coding: utf-8 -*-

from ...DataModel import Model

from abc import ABCMeta, abstractmethod
from typing import Type


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
	def query(self):
		pass

	@property
	@abstractmethod
	def args(self):
		pass
	