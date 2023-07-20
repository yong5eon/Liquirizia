# -*- coding: utf-8 -*-

__all__ = (
	'EventRunnerComplete'
)


class EventRunnerComplete(object):
	"""
	Event Runner Complete Interface
	"""
	def __call__(
		self,
		event: str,
		headers: dict = None,
		body=None,
		res=None,
	):
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))
