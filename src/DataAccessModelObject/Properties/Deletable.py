# -*- coding: utf-8 -*-

__all__ = (
	'Deletable'
)


class Deletable(object):
	"""
	Deletable Interface
	"""

	def delete(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented delete method'.format(self.__class__.__name__))
