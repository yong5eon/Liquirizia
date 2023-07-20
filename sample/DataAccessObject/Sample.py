# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import DataAccessObjectHelper
from Liquirizia.DataAccessObject import (
	DataAccessObjectConfiguration as DataAccessObjectConfigurationBase,
	DataAccessObject as DataAccessObjectBase,
	DataAccessObjectError,
)

import sys


class DataAccessObjectConfiguration(DataAccessObjectConfigurationBase):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		return


class DataAccessObject(DataAccessObjectBase):

	def __init__(self, conf: DataAccessObjectConfiguration):
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
			raise DataAccessObjectError('{} is not connected and initialized'.format(self.__class__.__name__))
		return self.data

	def set(self, data):
		if not isinstance(data, int):
			raise DataAccessObjectError('{} must be int'.format(data))
		self.data = data
		return self.data


if __name__ == '__main__':

	con = None

	try:
		# Set connection
		DataAccessObjectHelper.Set(
			'Sample',
			DataAccessObject,
			DataAccessObjectConfiguration(1, 2)
		)

		# Get Connection
		con = DataAccessObjectHelper.Get('Sample')
		print(con.get())  # expected print 3
		print(con.set(5))  # expected print 5
		print(con.set('a'))  # expected DataAccessObjectError
	except DataAccessObjectError as e:
		print(str(e), file=sys.stderr)
	except RuntimeError as e:
		print(str(e), file=sys.stderr)
