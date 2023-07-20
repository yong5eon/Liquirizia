# -*- coding: utf-8 -*-

__all__ = (
	'Consumer'
)


class Consumer(object):
	"""
	Consumer Interface of Event Broker
	"""
	def qos(self, count: int):
		raise NotImplementedError('{} must be implemented qos'.format(self.__class__.__name__))

	def consume(self, queue: str):
		raise NotImplementedError('{} must be implemented consume'.format(self.__class__.__name__))

	def run(self, interval: int = None):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))

	def stop(self):
		raise NotImplementedError('{} must be implemented stop'.format(self.__class__.__name__))
