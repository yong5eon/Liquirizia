# -*- coding: utf-8 -*-

__all__ = (
	'Index'
)


class Index(object):
	"""
	Data Access Object Interface for Index
	"""

	def create(self, index, *args, **kwargs):
		raise NotImplementedError('{} must be implemented create'.format(self.__class__.__name__))

	def delete(self, index):
		raise NotImplementedError('{} must be implemented delete'.format(self.__class__.__name__))

	def total(self, index):
		raise NotImplementedError('{} must be implemented count'.format(self.__class__.__name__))

	def set(self, index, *args, **kwargs):
		raise NotImplementedError('{} must be implemented set'.format(self.__class__.__name__))

	def get(self, index, id):
		raise NotImplementedError('{} must be implemented get'.format(self.__class__.__name__))

	def exists(self, index, id):
		raise NotImplementedError('{} must be implemented exists'.format(self.__class__.__name__))

	def count(self, index, *args, **kwargs):
		raise NotImplementedError('{} must be implemented search'.format(self.__class__.__name__))

	def query(self, index, *args, **kwargs):
		raise NotImplementedError('{} must be implemented search'.format(self.__class__.__name__))
