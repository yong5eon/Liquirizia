# -*- coding: utf-8 -*-

from Liquirizia.DataModel import Model

from abc import ABCMeta, abstractmethod

from .Executors import Executors
from .Executor import Executor
from .Mapper import Mapper
from .Filter import Filter

from typing import Type, Union, List, Dict

__all__ = (
	'Run'
)


class Run(metaclass=ABCMeta):
	"""Runnable Interface for Model"""
	@abstractmethod
	def run(
		self,
		executor: Type[Union[Executor, Executors]],
		mapper: Mapper = None,
		filter: Filter = None,
	) -> Type[Union[Model, List[Model], List[Dict]]]:
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
