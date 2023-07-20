# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error
from ..ErrorResponse import ErrorResponse

from ...Response import Response

__all__ = (
	'IsLessEqualTo'
)


class IsLessEqualTo(Pattern):
	def __init__(self, compare, error: Error = None, errorResponse: ErrorResponse = None):
		self.compare = compare
		self.error = error
		self.errorResponse = errorResponse
		return

	def __call__(self, parameter) -> (any, (Response, None)):
		try:
			if not parameter <= self.compare:
				if self.error:
					raise self.error(parameter, self.compare)
				raise RuntimeError('{} must be less equal to {}'.format(parameter, self.compare))
			return parameter, None
		except BaseException as e:
			if self.errorResponse:
				return parameter, self.errorResponse(parameter, self.compare)
			raise e
