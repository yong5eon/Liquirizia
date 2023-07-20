# -*- coding: utf-8 -*-

__all__ = (
	'Event'
)


class Event(object):
	"""
	Event Interface of Event Broker
	"""
	def ack(self):
		raise NotImplementedError('{} must be implemented ack'.format(self.__class__.__name__))

	def nack(self):
		raise NotImplementedError('{} must be implemented nack'.format(self.__class__.__name__))

	def reject(self):
		raise NotImplementedError('{} must be implemented reject'.format(self.__class__.__name__))

	def headers(self):
		raise NotImplementedError('{} must be implemented headers'.format(self.__class__.__name__))

	def header(self, key):
		raise NotImplementedError('{} must be implemented header'.format(self.__class__.__name__))

	@property
	def src(self):
		raise NotImplementedError('{} must be implemented src'.format(self.__class__.__name__))

	@property
	def id(self):
		raise NotImplementedError('{} must be implemented id'.format(self.__class__.__name__))

	@property
	def type(self):
		raise NotImplementedError('{} must be implemented event'.format(self.__class__.__name__))

	@property
	def body(self):
		raise NotImplementedError('{} must be implemented body'.format(self.__class__.__name__))
