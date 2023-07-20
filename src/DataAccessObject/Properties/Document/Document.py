# -*- coding: utf-8 -*-

__all__ = (
	'Document'
)


class Document(object):
	"""
	Data Access Object Interface for Document
	"""

	def create(self, doc, **kwargs):
		raise NotImplementedError('{} must be implemented create'.format(self.__class__.__name__))

	def set(self, doc, **kwargs):
		raise NotImplementedError('{} must be implemented set'.format(self.__class__.__name__))

	def get(self, doc, **kwargs):
		raise NotImplementedError('{} must be implemented get'.format(self.__class__.__name__))

	def query(self, doc, **kwargs):
		raise NotImplementedError('{} must be implemented find'.format(self.__class__.__name__))

	def remove(self, doc, **kwargs):
		raise NotImplementedError('{} must be implemented remove'.format(self.__class__.__name__))

	def delete(self, doc):
		raise NotImplementedError('{} must be implemented delete'.format(self.__class__.__name__))
