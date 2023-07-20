# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error

__all__ = (
	'IsRequiredInDictionary'
)


class IsRequiredInDictionary(Pattern):
	def __init__(self, *args, error: Error = None):
		self.args = args
		self.error = error
		return

	def __call__(self, parameter):
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
		return parameter
