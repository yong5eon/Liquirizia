# -*- coding: utf-8 -*-

from Liquirizia.DataAccessModelObject import (
	DataAccessModelObject,
	DataAccessModelObjectHelper,
	DataAccessModelObjectParameters
)
from Liquirizia.DataAccessModelObject.Properties import *

from Liquirizia.DataAccessObject import DataAccessObject, DataAccessObjectConfiguration

from Liquirizia.Template import Singleton

from random import randint


class SampleDataObject(Singleton):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.obj = {}
		return


class SampleDataAccessObjectConfiguration(DataAccessObjectConfiguration):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		return


class SampleDataAccessObject(DataAccessObject):
	def __init__(self, conf: SampleDataAccessObjectConfiguration):
		self.conf = conf
		self.src = None
		return

	def __del__(self):
		self.close()
		return

	def connect(self):
		self.src = SampleDataObject(self.conf.a, self.conf.b)
		return

	def close(self):
		self.src = None
		return


# Data Model Object for Initialize, UnInitialize, Create, Read, Update, Delete, Get, Set, Count
class SampleModelObject(
	DataAccessModelObject,
	Initializable,
	Gettable,
	Settable,
	Readable,
):
	def __init__(self, connection: DataAccessObject):
		self.con = connection
		return

	def initialize(self):
		for i in range(0, 10):
			self.con.src.obj[i] = randint(0, 100)
		return

	def get(self, key):
		if key not in self.con.src.obj.keys():
			raise RuntimeError('{} is not exist'.format(key))
		return self.con.src.obj[key]

	def set(self, key, value):
		self.con.src.obj[key] = value
		return

	def read(self):
		return self.con.src.obj.items()


if __name__ == '__main__':

	con = SampleDataAccessObject(SampleDataAccessObjectConfiguration(1, 2))
	con.connect()

	# with DataAccessModelObject
	obj = SampleModelObject(con)
	obj.initialize()

	for k, v in obj.read():
		print(k, v)

	obj.set(3, 10)  # set data
	print(obj.get(3))  # get data

	for k, v in obj.read():
		print(k, v)

	# with DataAccessModelObjectHelper
	DataAccessModelObjectHelper.Initialize(con, SampleModelObject)

	for k, v in DataAccessModelObjectHelper.Read(con, SampleModelObject):
		print(k, v)

	DataAccessModelObjectHelper.Set(con, SampleModelObject, DataAccessModelObjectParameters(3, 10))
	print(DataAccessModelObjectHelper.Get(con, SampleModelObject, DataAccessModelObjectParameters(3)))

	for k, v in DataAccessModelObjectHelper.Read(con, SampleModelObject):
		print(k, v)

	con.close()
