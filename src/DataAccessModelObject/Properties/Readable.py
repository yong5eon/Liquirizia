# -*- coding: utf-8 -*-

__all__ = (
	'Readable'
)


class Readable(object):
	"""
	Readable Interface
	"""

	def read(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented read method'.format(self.__class__.__name__))
