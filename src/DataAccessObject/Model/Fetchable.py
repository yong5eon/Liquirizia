# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Fetchable'
)


class Fetchable(metaclass=ABCMeta):
	"""Executable Interface for Model"""
	@abstractmethod
	def fetch(self, con, rows):
		raise NotImplementedError('{} must be implemented fetch'.format(self.__class__.__name__))
