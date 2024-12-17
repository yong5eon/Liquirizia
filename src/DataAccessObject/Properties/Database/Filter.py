# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from typing import Any

__all__ = (
	'Filter',
)


class Filter(metaclass=ABCMeta):
	"""Value Filter"""
	@abstractmethod
	def __call__(self, value: Any) -> Any:
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))
