# -*- coding: utf-8 -*-

from .Context import Context

from abc import ABCMeta, abstractmethod

__all__ = (
	'Cursor'
)


class Cursor(metaclass=ABCMeta):
	"""Cursor Interface for Database"""

	@abstractmethod
	def execute(self, sql, *args, **kwargs) -> Context:
		raise NotImplementedError('{} must be implemented execute'.format(self.__class__.__name__))

	@abstractmethod
	def executes(self, sql, *args, **kwargs) -> Context:
		raise NotImplementedError('{} must be implemented executes'.format(self.__class__.__name__))
	