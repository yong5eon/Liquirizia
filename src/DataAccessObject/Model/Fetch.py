# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Fetch'
)


class Fetch(metaclass=ABCMeta):
	"""Fetch Interface for Model"""
	@abstractmethod
	def fetch(self, cursor):
		raise NotImplementedError('{} must be implemented fetch'.format(self.__class__.__name__))