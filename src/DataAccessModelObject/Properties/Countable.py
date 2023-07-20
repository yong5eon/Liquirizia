# -*- coding: utf-8 -*-

__all__ = (
	'Countable'
)


class Countable(object):
	"""
	Countable Interface
	"""

	def count(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented count method'.format(self.__class__.__name__))
	
