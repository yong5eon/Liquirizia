# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from .Mapper import Mapper
from .Filter import Filter

__all__ = (
	'Fetch'
)


class Fetch(metaclass=ABCMeta):
	"""Fetchable Interface for Model"""
	@abstractmethod
	def fetch(
		self,
		cursor,
		mapper: Mapper = None,
		filter: Filter = None,
	):
		raise NotImplementedError('{} must be implemented fetch'.format(self.__class__.__name__))
