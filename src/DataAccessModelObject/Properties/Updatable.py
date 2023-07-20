# -*- coding: utf-8 -*-

__all__ = (
	'Updatable'
)


class Updatable(object):
	"""
	Updatable Interface
	"""

	def update(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented update method'.format(self.__class__.__name__))
