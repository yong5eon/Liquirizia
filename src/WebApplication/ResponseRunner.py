# -*- coding: utf-8 -*-

from .Response import Response

__all__ = (
	'ResponseRunner',
)


class ResponseRunner(object):
	"""
	"""
	def run(self, request: Response, body: any = None):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
