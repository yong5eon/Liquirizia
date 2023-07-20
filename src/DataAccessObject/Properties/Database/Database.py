# -*- coding: utf-8 -*-

__all__ = (
	'Database'
)


class Database(object):
	"""
	Data Access Object Interface for Database
	"""

	def begin(self):
		raise NotImplementedError('{} must be implemented begin'.format(self.__class__.__name__))

	def execute(self, sql, *args, **kwargs):
		raise NotImplementedError('{} must be implemented execute'.format(self.__class__.__name__))

	def affected(self):
		raise NotImplementedError('{} must be implemented affected'.format(self.__class__.__name__))

	def rows(self):
		raise NotImplementedError('{} must be implemented rows'.format(self.__class__.__name__))

	def commit(self):
		raise NotImplementedError('{} must be implemented commit'.format(self.__class__.__name__))

	def rollback(self):
		raise NotImplementedError('{} must be implemented rollback'.format(self.__class__.__name__))
