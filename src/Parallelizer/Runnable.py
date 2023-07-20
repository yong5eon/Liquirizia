# -*- coding: utf-8 -*-

__all__ = (
	'Runnable'
)


class Runnable(object):
	"""
	Runnable Interface for Parallelize
	"""

	def run(self):
		raise NotImplementedError('{} must be implemented run method.'.format(self.__class__.__name__))
