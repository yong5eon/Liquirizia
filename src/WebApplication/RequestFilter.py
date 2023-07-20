# -*- coding: utf-8 -*-

from .Request import Request
from .Response import Response

__all__ = (
	'RequestFilter',
)


class RequestFilter(object):
	"""
	"""
	def run(self, request: Request) -> tuple[Request, (Response, None)]:
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
