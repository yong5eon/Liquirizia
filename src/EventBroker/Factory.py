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
		return

	def connect(self) -> Connection:
		connection = self.object(self.conf)
		connection.connect()
		return connection

