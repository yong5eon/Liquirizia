# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from typing import Dict

__all__ = (
	'Filter',
)


class Filter(metaclass=ABCMeta):
	"""Row Filter Interface"""
	@abstractmethod
	def __call__(self, row: Dict) -> Dict:
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))
