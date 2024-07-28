# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Helper
from Liquirizia.DataAccessObject import (
	Configuration as BaseConfiguration,
	Connection as BaseConnection,
	Error,
)

import sys


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


if __name__ == '__main__':

	con = None

	try:
		# Set connection
		Helper.Set(
			'Sample',
			Connection,
			Configuration(1, 2)
		)

		# Get Connection
		con = Helper.Get('Sample')
		print(con.get())  # expected print 3
		print(con.set(5))  # expected print 5
		print(con.set('a'))  # expected Error
	except Error as e:
		print(str(e), file=sys.stderr)
	except RuntimeError as e:
		print(str(e), file=sys.stderr)
