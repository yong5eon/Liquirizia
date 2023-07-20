# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error
from ..ErrorResponse import ErrorResponse

from ...Response import Response

__all__ = (
	'IsRequiredInDictionary'
)


class IsRequiredInDictionary(Pattern):
	def __init__(self, *args, error: Error = None, errorResponse: ErrorResponse = None):
		self.args = args
		self.error = error
		self.errorResponse = errorResponse
		return

	def __call__(self, parameter) -> (any, (Response, None)):
		try:
			if not isinstance(parameter, dict):
				if self.error:
					raise self.error(parameter)
				raise RuntimeError('{} must be dict'.format(parameter))
			keys = parameter.keys()
			for arg in self.args:
				if arg not in keys:
					if self.error:
						raise self.error(parameter, arg)
					raise RuntimeError('{} is required in {}'.format(arg, parameter))
			return parameter, None
		except BaseException as e:
			if self.errorResponse:
				return parameter, self.errorResponse(parameter, self.args)
			raise e
