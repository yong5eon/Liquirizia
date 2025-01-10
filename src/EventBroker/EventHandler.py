# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'EventHandler'
)


class EventHandler(metaclass=ABCMeta):
	"""Event Handler Interface of Event Broker"""
	@abstractmethod
	def __call__(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))

