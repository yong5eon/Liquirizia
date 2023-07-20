# -*- coding: utf-8 -*-

from abc import (
	ABC,
	abstractmethod,
)

__all__ = (
	'Fixture'
)


class Fixture(ABC):
	"""Test Fixture Interface"""
	@abstractmethod
	def __init__(self, *args, **kwargs):
		pass
	@abstractmethod
	def __call__(self, *args, **kwargs):
		pass
