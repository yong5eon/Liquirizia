# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from typing import Any

__all__ = (
	'Mapper',
)


class Mapper(metaclass=ABCMeta):
	"""Column/Field Mapper"""
	@abstractmethod
	def __call__(self, str: str) -> str:
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))
