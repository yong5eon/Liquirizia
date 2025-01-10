# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from typing import Union

__all__ = (
	'Exchange'
)


class Exchange(metaclass=ABCMeta):
	"""Exchange Interface for Event Broker"""
	@abstractmethod
	def send(self, **kwargs):
		raise NotImplementedError('{} must be implemented send'.format(self.__class__.__name__))

