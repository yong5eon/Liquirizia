# -*- coding: utf-8 -*-

from .Event import Event

__all__ = (
	'Callback'
)


class Callback(object):
	"""
	Callback Interface of Event Broker
	"""
	def __call__(self, event: Event):
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))