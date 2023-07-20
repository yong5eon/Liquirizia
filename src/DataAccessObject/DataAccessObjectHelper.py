# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .DataAccessObject import DataAccessObject
from .DataAccessObjectConfiguration import DataAccessObjectConfiguration

__all__ = (
	'DataAccessObjectHelper'
)


class DataAccessObjectHelper(Singleton):
	"""
	Data Access Object Helper Class
	"""
	def onInit(self):
		self.objects = {}
		return

	@classmethod
	def Get(cls, key: str) -> (DataAccessObject, None):
		helper = cls()
		return helper.get(key)

	def get(self, key, connect: bool=True) -> (DataAccessObject, None):
		if key not in self.objects:
			return None
		con = self.objects[key][0](self.objects[key][1])
		con.connect()
		return con

	@classmethod
	def Set(cls, key, o: type(DataAccessObject), conf: DataAccessObjectConfiguration):
		helper = cls()
		helper.set(key, o, conf)
		return

	def set(self, key, o: type(DataAccessObject), conf: DataAccessObjectConfiguration):
		if not isinstance(o, type(DataAccessObject)):
			raise RuntimeError('{} must be type of class based DataAccessObject'.format(o))
		if not isinstance(conf, DataAccessObjectConfiguration):
			raise RuntimeError('{} must be based DataAccessObjectConfiguration'.format(conf))
		self.objects[key] = (o, conf)
		return
