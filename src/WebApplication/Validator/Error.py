# -*- coding: utf-8 -*-

from ..Error import Error as WebApplicationError

__all__ = (
	'Error'
)


class Error(object):
	"""
	Error Interface Class for Validator of WebApplication
	"""
	def __call__(self, parameter, *args, **kwargs) -> WebApplicationError:
		raise NotImplementedError('{} must be implemented __call__ and must return exception class based Error of WebApplication'.format(self.__class__.__name__))
