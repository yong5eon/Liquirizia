# -*- coding: utf-8 -*-

__all__ = (
	'Response'
)


class Response(object):
	"""
	Response Interface of Event Broker
	"""
	def headers(self):
		raise NotImplementedError('{} must be implemented headers'.format(self.__class__.__name__))

	def header(self, key):
		raise NotImplementedError('{} must be implemented header'.format(self.__class__.__name__))

	@property
	def id(self):
		raise NotImplementedError('{} must be implemented id'.format(self.__class__.__name__))

	@property
	def type(self):
		raise NotImplementedError('{} must be implemented event'.format(self.__class__.__name__))

	@property
	def body(self):
		raise NotImplementedError('{} must be implemented body'.format(self.__class__.__name__))
