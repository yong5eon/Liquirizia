# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.DataAccessObject import Helper
from Liquirizia.DataAccessObject import (
	Configuration as BaseConfiguration,
	Connection as BaseConnection,
	Error,
)

class Configuration(BaseConfiguration):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		return


class Connection(BaseConnection):

	def __init__(self, conf: Configuration):
		self.conf = conf
		self.data = None
		return

	def __del__(self):
		self.close()
		return

	def connect(self):
		self.data = self.conf.a + self.conf.b
		return

	def close(self):
		self.data = None
		return

	def get(self):
		if self.data is None:
			raise Error('{} is not connected and initialized'.format(self.__class__.__name__))
		return self.data

	def set(self, data):
		if not isinstance(data, int):
			raise Error('{} must be int'.format(data))
		self.data = data
		return self.data
	

class TestDataAccessObject(Case):
	@classmethod
	def setUpClass(cls):
		Helper.Set(
			'Sample',
			Connection,
			Configuration(1, 2)
		)
		return super().setUpClass()

	@Parameterized(
			{'v': 1},
			{'v': 2},
			{'v': 3},
	)	
	def test(self, v):
		con = Helper.Get('Sample')
		ASSERT_IS_EQUAL(con.get(), 3)
		con.set(v)
		ASSERT_IS_EQUAL(con.get(), v)
		with ASSERT_EXCEPT(Error) as e:
			con.set('a')
			ASSERT_IS_EQUAL(e.exception, Error)
