# -*- coding: utf-8 -*-

from Liquirizia.EventRunner import EventRunnerProperties
from Liquirizia.EventRunner.Types import EventTimer, EventInterval
from Liquirizia.EventRunner.Errors import NotSupportedTypeError

__all__ = (
	'EventContext'
)


class EventContext(object):
	"""
	Event Context Class
	"""
	def __init__(self):
		self.context = {}
		return

	def add(self, properties: EventRunnerProperties):
		if not isinstance(properties.type, (EventTimer, EventInterval)):
			raise NotSupportedTypeError(properties.type.__class__.__name__)
		self.context[properties.type.event] = properties
		return

	def events(self):
		return self.context.items()

	def match(self, event: str):
		if event not in self.context:
			return None
		return self.context[event]
