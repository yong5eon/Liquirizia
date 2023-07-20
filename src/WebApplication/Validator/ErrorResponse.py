# -*- coding: utf-8 -*-

from ..Response import Response

__all__ = (
	'ErrorResponse'
)


class ErrorResponse(object):
	"""
	Error Response Interface Class for Validator of WebApplication
	"""
	def __call__(self, parameter, *args, **kwargs) -> Response:
		raise NotImplementedError('{} must be implemented __call__ and must return response class based Response of WebApplication'.format(self.__class__.__name__))
