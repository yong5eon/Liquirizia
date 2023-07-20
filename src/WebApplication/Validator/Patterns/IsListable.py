# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error
from ..ErrorResponse import ErrorResponse

from ...Response import Response

__all__ = (
	'IsListable'
)


class IsListable(Pattern):
	def __init__(self, *args, error: Error = None, errorResponse: ErrorResponse = None):
		self.patterns = args
		self.error = error
		self.errorResponse = errorResponse
		return

	def __call__(self, parameter) -> (any, (Response, None)):
		try:
			if not isinstance(parameter, (list, tuple)):
				if self.error:
					raise self.error(parameter)
				raise RuntimeError('{} must be listable'.format(parameter))
			for pattern in self.patterns:
				for i, e in enumerate(parameter):
					parameter[i], response = pattern(e)
					if response:
						return parameter, response
			return parameter, None
		except BaseException as e:
			if self.errorResponse:
				return parameter, self.errorResponse(parameter)
			raise e
