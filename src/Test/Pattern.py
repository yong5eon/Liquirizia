# -*- coding: utf-8 -*-

from .Case import Case

from abc import (
	ABC,
	abstractmethod,
)

__all__ = (
	'Pattern'
)


class Pattern(ABC):
	"""Test Pattern Interface"""
	@abstractmethod
	def __init__(self, *args, **kwargs):
		pass
	@abstractmethod
	def __call__(self, case: Case):
		pass
	@abstractmethod
	def __str__(self):
		pass
