# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from .Executors import Executors
from .Executor import Executor

from ...DataModel import Model

from typing import Union

__all__ = (
	'Executable'
)


class Executable(metaclass=ABCMeta):
	"""Executable Interface for Model"""
	@abstractmethod
	def runs(self, executors: Executors) -> None:
		raise NotImplementedError('{} must be implemented runs'.format(self.__class__.__name__))
	
	@abstractmethod
	def run(self, executor: Executor, cb: callable = None) -> Union[Model, list[Model], list]:
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
