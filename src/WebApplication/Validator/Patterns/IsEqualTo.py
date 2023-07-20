# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error
from ..ErrorResponse import ErrorResponse

from ...Response import Response

__all__ = (
	'IsEqualTo'
)


class IsEqualTo(Pattern):
	def __init__(self, equal, error: Error = None, errorResponse: ErrorResponse = None):
		self.equal = equal
		self.error = error
		self.errorResponse = errorResponse
		return

	def __call__(self, parameter) -> (any, (Response, None)):
		try:
			if not parameter == self.equal:
				if self.error:
					raise self.error(parameter, self.equal)
				raise RuntimeError('{} must equal to {}'.format(parameter, self.equal))
			return parameter, None
		except BaseException as e:
			if self.errorResponse:
				return parameter, self.errorResponse(parameter, self.equal)
			raise e
