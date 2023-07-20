# -*- coding: utf-8 -*-

from .Pattern import Pattern

__all__ = (
	'Validator'
)


class Validator(object):
	"""
	Validator Class
	"""
	def __init__(self, *args):
		for pattern in args:
			if not isinstance(pattern, Pattern):
				raise RuntimeError('{} must be based {}'.format(pattern, Pattern))
		self.patterns = args
		return

	def __call__(self, parameter):
		for pattern in self.patterns:
			parameter = pattern(parameter)
		return parameter

	def __repr__(self):
		return 'Validator({})'.format(
			', '.join([repr(p) for p in self.patterns])
		)
