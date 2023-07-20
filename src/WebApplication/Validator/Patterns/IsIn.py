# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error
from ..ErrorResponse import ErrorResponse

from ...Response import Response

__all__ = (
	'IsIn'
)


class IsIn(Pattern):
	def __init__(self, *args, error: Error = None, errorResponse: ErrorResponse = None):
		self.compares = args
		self.error = error
		self.errorResponse = errorResponse
		return

	def __call__(self, parameter) -> (any, (Response, None)):
		try:
			if parameter not in self.compares:
				if self.error:
					raise self.error(parameter, self.compares)
				raise RuntimeError('{} must be in {}'.format(parameter, self.compares))
			return parameter, None
		except BaseException as e:
			if self.errorResponse:
				return parameter, self.errorResponse(parameter, args)
			raise e
