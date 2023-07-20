# -*- coding: utf-8 -*-

from ..EventType import EventType

__all__ = (
	'EventInterval'
)


class EventInterval(EventType):
	"""
	Interval Event Type Class
	"""
	def __init__(self, event: str, interval: int, headers: dict = None, body=None):
		self.__props__ = {
			'event': event,
			'interval': interval,
			'headers': headers,
			'body': body,
		}
		return

	@property
	def event(self):
		return self.__props__['event']

	@property
	def interval(self):
		return self.__props__['interval']

	@property
	def headers(self):
		return self.__props__['headers']

	@property
	def body(self):
		return self.__props__['body']
