# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'IsTuple'
)


class IsTuple(Pattern):
	def __init__(self, *args, error: Error = None):
		self.patterns = args
		self.error = error
		return

	def __call__(self, parameter):
		if not isinstance(parameter, tuple):
			if self.error:
				raise self.error(parameter)
			raise RuntimeError('{} must be tuple'.format(parameter))
		
		validParameter = tuple()
		for pattern in self.patterns:
			for element in parameter:
				validParameter += (pattern(element),)
		
		return validParameter
