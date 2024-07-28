# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Document'
)


class Document(metaclass=ABCMeta):
	"""Interface for Document"""

	@abstractmethod
	def create(self, doc, **kwargs):
		raise NotImplementedError('{} must be implemented create'.format(self.__class__.__name__))

	@abstractmethod
	def set(self, doc, **kwargs):
		raise NotImplementedError('{} must be implemented set'.format(self.__class__.__name__))

	@abstractmethod
	def get(self, doc, **kwargs):
		raise NotImplementedError('{} must be implemented get'.format(self.__class__.__name__))

	@abstractmethod
	def query(self, doc, **kwargs):
		raise NotImplementedError('{} must be implemented find'.format(self.__class__.__name__))

	@abstractmethod
	def remove(self, doc, **kwargs):
		raise NotImplementedError('{} must be implemented remove'.format(self.__class__.__name__))
