# -*- coding: utf-8 -*-

__all__ = (
	'UnInitializable'
)


class UnInitializable(object):
	"""
	UnInitializable Interface
	"""

	def uninitialize(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented uninitialize method'.format(self.__class__.__name__))
