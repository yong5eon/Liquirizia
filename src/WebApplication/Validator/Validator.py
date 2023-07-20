# -*- coding: utf-8 -*-

from Liquirizia.Validator import Validator as Base

from .Pattern import Pattern

__all__ = (
	'Validator'
)


class Validator(Base):
	"""
	Validator Class for Web Application
	"""
	def __init__(self, *args):
		super(Validator, self).__init__(*args)
		for pattern in self.patterns:
			if not isinstance(pattern, Pattern):
				raise RuntimeError('{} must be based {}'.format(pattern, Pattern))
		return

	def __call__(self, parameter):
		for pattern in self.patterns:
			parameter, response = pattern(parameter)
			if response:
				return parameter, response
		return parameter, None
