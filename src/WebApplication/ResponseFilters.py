# -*- coding: utf-8 -*-

from .Response import Response
from .ResponseFilter import ResponseFilter

__all__ = (
	'ResponseFilters',
)


class ResponseFilters(ResponseFilter):
	"""
	"""
	def run(self, response: Response) -> Response:
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
