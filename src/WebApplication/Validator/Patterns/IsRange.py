# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error
from ..ErrorResponse import ErrorResponse

from ...Response import Response

__all__ = (
	'IsRange'
)


class IsRange(Pattern):
	def __init__(self, start, stop=None, step=None, error: Error = None, errorResponse: ErrorResponse = None):
		self.range = [start]
		if stop:
			self.range.append(stop)
		if step:
			self.range.append(step)
		self.start = start
		self.stop = stop
		self.step = step
		self.error = error
		self.errorResponse = errorResponse
		return

	def __call__(self, parameter) -> (any, (Response, None)):
		try:
			if parameter not in [v for v in range(*self.range)]:
				if self.error:
					raise self.error(parameter, self.start, self.stop, self.range)
				raise RuntimeError('{} must be in the range {}'.format(
					parameter,
					'between {} to {}{}'.format(
						self.start if self.stop else 0,
						self.stop if self.stop else self.start,
						', in increments of {}'.format(self.step) if self.step else ''
					),
				))
			return parameter, None
		except BaseException as e:
			if self.errorResponse:
				return parameter, self.errorResponse(parameter, self, self.start, self.stop, self.step)
			raise e
