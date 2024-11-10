# -*- coding: utf-8 -*-

from .Configuration import Configuration
from .Connection import Connection

from typing import Type

__all__ = (
	'Factory'
)


class Factory(object):
	"""Factory Class for Event Broker"""

	def __init__(self, object: Type[Connection], conf: Configuration):
		self.object = object
		self.conf = conf
		self.connection = None
		return

	def connect(self) -> Connection:
		if not self.connection:
			self.connection = self.object(self.conf)
		self.connection.connect()
		return self.connection
