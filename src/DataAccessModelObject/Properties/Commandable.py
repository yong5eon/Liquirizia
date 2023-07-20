# -*- coding: utf-8 -*-

__all__ = (
	'Commandable'
)


class Commandable(object):
	"""
	Commandable Interface
	"""

	def command(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented command method'.format(self.__class__.__name__))
