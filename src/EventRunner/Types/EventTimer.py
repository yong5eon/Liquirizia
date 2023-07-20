# -*- coding: utf-8 -*-

from ..EventType import EventType

__all__ = (
	'EventTimer'
)


class EventTimer(EventType):
	"""
	Timer Event Type Class with Cron Pattern

	Pattern :
	Second Minute Hour DayOfMonth Month DayOfWeek Year
	"""
	PATTERN = [
		'Second',
		'Minute',
		'Hour',
		'DayOfMonth',
		'Month'
		'DayOfWeek',
		'Year'
	]

	def __init__(self, event: str, pattern: str, headers: dict = None, body=None):
		self.__props__ = {
			'event': event,
			'patternString': pattern,
			'pattern': {},
			'headers': headers,
			'body': body,
		}
		ps = pattern.split(' ')
		for i, s in enumerate(ps):
			self.__props__['pattern'][self.PATTERN[i]] = s
		return

	@property
	def event(self):
		return self.__props__['event']

	@property
	def pattern(self):
		return self.__props__['patternString']

	@property
	def headers(self):
		return self.__props__['headers']

	@property
	def body(self):
		return self.__props__['body']

	@property
	def second(self):
		return self.__props__['pattern']['Second'] if 'Second' in self.__props__['pattern'] else None

	@property
	def minute(self):
		return self.__props__['pattern']['Minute'] if 'Minute' in self.__props__['pattern'] else None

	@property
	def hour(self):
		return self.__props__['pattern']['Hour'] if 'Hour' in self.__props__['pattern'] else None

	@property
	def dayOfMonth(self):
		return self.__props__['pattern']['DayOfMonth'] if 'DayOfMonth' in self.__props__['pattern'] else None

	@property
	def month(self):
		return self.__props__['pattern']['Month'] if 'Month' in self.__props__['pattern'] else None

	@property
	def dayOfWeek(self):
		return self.__props__['pattern']['DayOfWeek'] if 'DayOfWeek' in self.__props__['pattern'] else None

	@property
	def year(self):
		return self.__props__['pattern']['Year'] if 'Year' in self.__props__['pattern'] else None
