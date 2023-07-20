# -*- coding: utf-8 -*-

from .Request import Request

__all__ = (
	'RequestRunner',
)


class RequestRunner(object):
	"""
	Request Runner Interface
	"""
	def __init__(self, request: Request, parameters):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

	def run(self, body=None):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
