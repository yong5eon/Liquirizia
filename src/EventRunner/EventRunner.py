# -*- coding: utf-8 -*-

__all__ = (
	'EventRunner',
)


class EventRunner(object):
	"""
	Event Runner Interface
	"""
	def __init__(self, event: str, headers: dict = None):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

	def run(self, body=None):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
