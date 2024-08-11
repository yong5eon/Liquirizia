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
	def run(self, executor: Union[Executor, Executors], cb: callable = None) -> Union[Model, list[Model], list]:
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
