# -*- coding: utf-8 -*-

__all__ = (
	'Cache'
)


class Cache(object):
	"""
	Data Access Object Interface for Cache
	"""
	def keys(self, key):
		raise NotImplementedError('{} must be implemented keys'.format(self.__class__.__name__))

	def exists(self, key):
		raise NotImplementedError('{} must be implemented exist'.format(self.__class__.__name__))

	def get(self, key):
		raise NotImplementedError('{} must be implemented get'.format(self.__class__.__name__))

	def set(self, key, value, expires=None):
		raise NotImplementedError('{} must be implemented set'.format(self.__class__.__name__))

	def expire(self, key, seconds):
		raise NotImplementedError('{} must be implemented expire'.format(self.__class__.__name__))

	def persist(self, key):
		raise NotImplementedError('{} must be implemented persist'.format(self.__class__.__name__))

	def delete(self, key):
		raise NotImplementedError('{} must be implemented delete'.format(self.__class__.__name__))
