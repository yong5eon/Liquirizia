# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .Factory import Factory
from .Configuration import Configuration
from .Connection import Connection

from typing import Type

__all__ = (
	'Helper'
)


class Helper(Singleton):
	"""
	Event Broker Helper Class
	"""

	def __init__(self):
		self.brokers = {}
		return

	def set(self, key: str, object: Type[Connection], conf: Configuration):
		self.brokers[key] = Factory(object, conf)
		return

	@classmethod
	def Set(cls, key: str, object: Type[Connection],  conf: Configuration):
		helper = cls()
		return helper.set(key, object, conf)

	def get(self, key: str) -> Connection:
		if key not in self.brokers:
			return None
		broker = self.brokers[key]
		return broker.connect()

	@classmethod
	def Get(cls, key: str) -> Connection:
		helper = cls()
		return helper.get(key)
