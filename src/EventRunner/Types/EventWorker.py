# -*- coding: utf-8 -*-

from ..EventType import EventType

__all__ = (
	'EventWorker'
)


class EventWorker(EventType):
	"""
	Event Worker Type Class
	"""
	def __init__(self, event: str, name: str, queue: str, count: int = 1, size: int = 0, vhost: str = '/'):
		self.__props__ = {
			'event': event,
			'name': name,
			'queue': queue,
			'count': count,
			'size': size,
			'vhost': vhost
		}
		return

	@property
	def event(self):
		return self.__props__['event']

	@property
	def broker(self):
		return self.__props__['name']

	@property
	def name(self):
		return self.__props__['name']

	@property
	def queue(self):
		return self.__props__['queue']

	@property
	def count(self):
		return self.__props__['count']

	@property
	def size(self):
		return self.__props__['size']

	@property
	def vhost(self):
		return self.__props__['vhost']
