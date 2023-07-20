# -*- coding: utf-8 -*-

__all__ = (
	'Initializable'
)


class Initializable(object):
	"""
	Initializable Interface
	"""

	def initialize(self):
		raise NotImplementedError('{} must be implemented initialize method'.format(self.__class__.__name__))
