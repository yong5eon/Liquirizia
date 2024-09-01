# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .Connection import Connection
from .Configuration import Configuration

from typing import Type

__all__ = (
	'Helper'
)


class Helper(Singleton):
	"""Helper Class"""

	def __init__(self):
		self.objects = {}
		return

	@classmethod
	def Get(cls, key: str) -> Connection:
		helper = cls()
		return helper.get(key)

	def get(self, key, connect: bool=True) -> Connection:
		if key not in self.objects:
			return None
		con = self.objects[key][0](self.objects[key][1])
		con.connect()
		return con

	@classmethod
	def Set(cls, key, o: Type[Connection], conf: Configuration):
		helper = cls()
		helper.set(key, o, conf)
		return

	def set(self, key, o: Type[Connection], conf: Configuration):
		if not isinstance(o, type(Connection)):
			raise RuntimeError('{} must be type of class based Connection'.format(o))
		if not isinstance(conf, Configuration):
			raise RuntimeError('{} must be based Configuration'.format(conf))
		self.objects[key] = (o, conf)
		return
