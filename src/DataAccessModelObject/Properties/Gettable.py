# -*- coding: utf-8 -*-

__all__ = (
	'Gettable'
)


class Gettable(object):
	"""
	Gettable Interface
	"""

	def get(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented get method'.format(self.__class__.__name__))
