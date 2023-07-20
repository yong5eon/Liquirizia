# -*- coding: utf-8 -*-

from .Configuration import Configuration
from .Connection import Connection

__all__ = (
	'EventBrokerFactory'
)


class EventBrokerFactory(object):
	"""
	Event Broker Factory Class
	"""

	def __init__(self, object: type(Connection), conf: Configuration, persistent: bool = False):
		self.object = object
		self.conf = conf
		self.connection = None
		self.persistent = persistent
		return

	def connect(self):
		if not self.persistent:
			connection = self.object(self.conf)
			connection.connect()
			return connection
		if not self.connection:
			self.connection = self.object(self.conf)
		self.connection.connect()
		return self.connection
