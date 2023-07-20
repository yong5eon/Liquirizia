# -*- coding: utf-8 -*-

__all__ = (
	'EventType'
)


class EventType(object):
	"""
	Event Type Interface
	"""

	@property
	def event(self):
		raise NotImplementedError('{} must be implemented event property'.format(self.__class__.__name__))
