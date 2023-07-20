# -*- coding: utf-8 -*-

__all__ = (
	'Synchronized'
)


class Synchronized(object):
	"""
	Synchronized Interface for Parallelize
	"""

	def initialize(self):
		raise NotImplementedError('{} class has to declare acquire method to initialize lock.'.format(self.__class__.__name__))

	def acquire(self):
		raise NotImplementedError('{} class has to declare acquire method to acquire lock.'.format(self.__class__.__name__))

	def release(self):
		raise NotImplementedError('{} class has to declare acquire method to release lock.'.format(self.__class__.__name__))

	def lock(self):
		raise NotImplementedError('{} class has to declare acquire method to lock.'.format(self.__class__.__name__))

	def delete(self):
		raise NotImplementedError('{} class has to declare acquire method to delete lock.'.format(self.__class__.__name__))
