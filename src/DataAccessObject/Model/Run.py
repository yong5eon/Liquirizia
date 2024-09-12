# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from .Executors import Executors
from .Executor import Executor

from ...DataModel import Model

from typing import Union, Sequence

__all__ = (
	'Run'
)


class Run(metaclass=ABCMeta):
	"""Runnable Interface for Model"""
	@abstractmethod
	def run(self, executor: Union[Executor,Executors]) -> Union[Model,Sequence,Sequence[Model]]:
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))