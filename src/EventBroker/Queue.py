# -*- coding: utf-8 -*-

__all__ = (
	'Queue'
)


class Queue(object):
	"""
	Queue Interface for Event Broker
	"""
	def declare(self, queue, **kwargs):
		raise NotImplementedError('{} must be implemented declare'.format(self.__class__.__name__))

	def bind(self, topic, event):
		raise NotImplementedError('{} must be implemented bind'.format(self.__class__.__name__))

	def send(
		self,
		event,
		body=None,
		format=None,
		charset=None,
		headers=None,
		priority=None,
		expiration=None,
		timestamp=None,
		persistent=True,
		id=None,
	):
		raise NotImplementedError('{} must be implemented send'.format(self.__class__.__name__))

	def qos(self, count: int):
		raise NotImplementedError('{} must be implemented qos'.format(self.__class__.__name__))

	def recv(self, timeout: int = None):
		raise NotImplementedError('{} must be implemented recv'.format(self.__class__.__name__))

	def unbind(self, topic, event):
		raise NotImplementedError('{} must be implemented unbind'.format(self.__class__.__name__))

	def remove(self):
		raise NotImplementedError('{} must be implemented remove'.format(self.__class__.__name__))
