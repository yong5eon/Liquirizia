# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from ...DataModel import Model

__all__ = (
	'Executor'
)


class Executor(metaclass=ABCMeta):
	"""Executor Interface for Data Model"""

	@abstractmethod
	def __init__(self, o: type[Model]):
		pass

	@property
	@abstractmethod
	def query(self):
		pass

	@property
	@abstractmethod
	def args(self):
		pass
	