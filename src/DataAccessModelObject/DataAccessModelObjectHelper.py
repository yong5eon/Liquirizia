# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from Liquirizia.DataAccessObject import DataAccessObject

from .DataAccessModelObject import DataAccessModelObject
from .DataAccessModelObjectParameters import DataAccessModelObjectParameters

from .Properties import Initializable
from .Properties import UnInitializable
from .Properties import Creatable
from .Properties import Readable
from .Properties import Updatable
from .Properties import Deletable
from .Properties import Gettable
from .Properties import Settable
from .Properties import Commandable
from .Properties import Queryable
from .Properties import Countable

__all__ = (
	'DataAccessModelObjectHelper'
)


class DataAccessModelObjectHelper(Singleton):
	"""
	Data Model Helper Class
	"""

	def __init__(self):
		return

	@classmethod
	def Initialize(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.initialize(connection, DataAccessModelObject, parameters)

	def initialize(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if Initializable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not realized Initializable interface'.format(DataAccessModelObject.__name__))

		obj = DataAccessModelObject(connection)
		return obj.initialize(*parameters.args, **parameters.kwargs)

	@classmethod
	def UnInitialize(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.uninitialize(connection, DataAccessModelObject, parameters)

	def uninitialize(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if UnInitializable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not realized of UnInitializable interface'.format(DataAccessModelObject.__name__))

		obj = DataAccessModelObject(connection)
		return obj.uninitialize(*parameters.args, **parameters.kwargs)

	@classmethod
	def Create(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.create(connection, DataAccessModelObject, parameters)

	def create(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if Creatable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not realized of Creatable interface'.format(DataAccessModelObject.__name__))

		obj = DataAccessModelObject(connection)
		return obj.create(*parameters.args, **parameters.kwargs)

	@classmethod
	def Read(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.read(connection, DataAccessModelObject, parameters)

	def read(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if Readable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not realized of Readable interface'.format(DataAccessModelObject.__name__))

		obj = DataAccessModelObject(connection)
		return obj.read(*parameters.args, **parameters.kwargs)

	@classmethod
	def Update(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.update(connection, DataAccessModelObject, parameters)

	def update(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if Updatable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not realized of Updatable interface'.format(DataAccessModelObject.__name__))

		obj = DataAccessModelObject(connection)
		return obj.update(*parameters.args, **parameters.kwargs)

	@classmethod
	def Delete(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.delete(connection, DataAccessModelObject, parameters)

	def delete(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if Deletable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not realized of Deletable interface'.format(DataAccessModelObject.__name__))

		obj = DataAccessModelObject(connection)
		return obj.delete(*parameters.args, **parameters.kwargs)

	@classmethod
	def Get(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.get(connection, DataAccessModelObject, parameters)

	def get(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if Gettable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not realized of Gettable interface'.format(DataAccessModelObject.__name__))

		obj = DataAccessModelObject(connection)
		return obj.get(*parameters.args, **parameters.kwargs)

	@classmethod
	def Set(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.set(connection, DataAccessModelObject, parameters)

	def set(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if Settable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not realized of Settable interface'.format(DataAccessModelObject.__name__))

		obj = DataAccessModelObject(connection)
		return obj.set(*parameters.args, **parameters.kwargs)
	
	@classmethod
	def Count(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.count(connection, DataAccessModelObject, parameters)
	
	def count(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if Countable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not Countable'.format(DataAccessModelObject.__name__))
		
		obj = DataAccessModelObject(connection)
		return obj.count(*parameters.args, **parameters.kwargs)

	@classmethod
	def Command(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.command(connection, DataAccessModelObject, parameters)

	def command(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if Commandable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not realized of Commandable interface'.format(DataAccessModelObject.__name__))

		obj = DataAccessModelObject(connection)
		return obj.command(*parameters.args, **parameters.kwargs)

	@classmethod
	def Query(
		DataAccessModelObjectHelper,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		helper = DataAccessModelObjectHelper()
		return helper.query(connection, DataAccessModelObject, parameters)

	def query(
		self,
		connection: DataAccessObject,
		DataAccessModelObject: type(DataAccessModelObject),
		parameters: DataAccessModelObjectParameters = DataAccessModelObjectParameters()
	):
		if Queryable not in DataAccessModelObject.__bases__:
			raise RuntimeError('{} is not Queryable'.format(DataAccessModelObject.__name__))

		obj = DataAccessModelObject(connection)
		return obj.query(*parameters.args, **parameters.kwargs)
