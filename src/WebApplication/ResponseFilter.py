# -*- coding: utf-8 -*-

from .Response import Response

__all__ = (
	'ResponseFilter',
)


class ResponseFilter(object):
	"""
	"""
	def __init__(self, *args):
		self.filters = args
		return

	def run(self, response: Response) -> Response:
		for f in self.filters:
			response = f.run(response)
		return response
