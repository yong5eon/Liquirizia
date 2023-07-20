# -*- coding: utf-8 -*-

__all__ = (
	'EventRunnerError'
)


class EventRunnerError(object):
	"""
	Event Runner Error Interface
	"""
	def __call__(
		self,
		event: str,
		headers: dict = None,
		body=None,
		error=None
	):
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))
