# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'ModelToString',
)


class ModelToString(ABC):
	"""Abstract Exchange Model To String Class"""
	@abstractmethod
	def __call__(self):
		pass
