# -*- coding: utf-8 -*-

from Liquirizia.DataModel import Model

from abc import ABCMeta, abstractmethod

from .Filter import Filter

from typing import Union, Dict, List, Type

__all__ = (
	'Fetch'
)


class Fetch(metaclass=ABCMeta):
	"""Fetchable Interface for Model"""
	@abstractmethod
	def fetch(
		self,
		cursor,
		filter: Filter = None,
		fetch: Type[Model] = None,
	) -> Union[Dict, Model, List[Dict], List[Model]]:
		raise NotImplementedError('{} must be implemented fetch'.format(self.__class__.__name__))

