# -*- coding: utf-8 -*-

__all__ = (
	'Queryable'
)


class Queryable(object):
	"""
	Queryable Interface
	"""

	def query(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented query method'.format(self.__class__.__name__))
