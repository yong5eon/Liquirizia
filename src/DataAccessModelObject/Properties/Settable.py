# -*- coding: utf-8 -*-

__all__ = (
	'Settable'
)


class Settable(object):
	"""
	Settable Interface
	"""

	def set(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented set method'.format(self.__class__.__name__))
