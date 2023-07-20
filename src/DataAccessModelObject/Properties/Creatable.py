# -*- coding: utf-8 -*-

__all__ = (
	'Creatable'
)


class Creatable(object):
	"""
	Creatable Interface
	"""

	def create(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented create method'.format(self.__class__.__name__))
