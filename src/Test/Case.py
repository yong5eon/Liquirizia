# -*- coding: utf-8 -*-

from abc import (
	ABC,
	abstractmethod,
)

__all__ = (
	'Case'
)


class Case(ABC):
	"""Test Case Interface"""
	@abstractmethod
	def __init__(self, *args, **kwargs):
		pass

	@abstractmethod
	def __call__(self):
		pass

	@abstractmethod
	def __str__(self):
		pass
