# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Connection as BaseConnection
from Liquirizia.DataAccessObject.Properties.Database import (
	Database,
	Executors,
	Executor,
	Run,
	Fetch,
	Mapper,
	Filter,
)

from Liquirizia.DataModel import Model

from .Configuration import Configuration
from .Context import Context
from .Cursor import Cursor
from .Session import Session

from sqlite3 import connect, Row

from typing import Union, Type

__all__ = (
	'DatabaseAccessObject'
)


class Connection(BaseConnection, Database, Run):
	"""Connection Class for Sqlite"""

	def __init__(self, conf: Configuration):
		self.conf = conf
		self.connection = None
		return

	def __del__(self):
		if not self.connection:
			return
		self.close()
		return

	def connect(self):
		self.connection = connect(
			self.conf.path,
			isolation_level=None if self.conf.autocommit else 'DEFERRED',
			check_same_thread=False,
		)
		self.connection.row_factory = Row
		return

	def close(self):
		if self.conf.autocommit:
			self.commit()

		if not self.cursor:
			self.cursor.close()
			del self.cursor
			self.cursor = None

		if not self.connection:
			self.connection.close()
			del self.connection
			self.connection = None
		return

	def begin(self):
		pass

	def execute(self, sql, *args):
		cursor = self.connection.cursor()
		cursor.execute(sql, args)
		return Context(cursor)
	
	def executes(self, sql, *args):
		cursor = self.connection.cursor()
		cursor.executemany(sql, args)
		return Context(cursor)

	def run(
		self,
		executor: Union[Executor,Executors],
		mapper: Mapper = None,
		filter: Filter = None,
		fetch: Type[Model] = None,
	):
		cursor = self.connection.cursor()
		def execs(execs: Executors):
			__ = []
			for query, args in executor:
				cursor.execute(query, args)
				if not isinstance(executor, Fetch): continue
				rows = executor.fetch(Cursor(cursor), mapper=mapper, filter=filter, fetch=fetch)
				__.extend(rows)
			return __
		def exec(exec: Executor):
			cursor.execute(executor.query, executor.args)
			if not isinstance(exec, Fetch): return
			return exec.fetch(Cursor(cursor), mapper=mapper, filter=filter, fetch=fetch)
		if isinstance(executor, Executors): return execs(executor)
		if isinstance(executor, Executor): return exec(executor)
		raise RuntimeError('{} is not executor or executors'.format(executor.__class__.__name__))
		
	def cursor(self) -> Cursor:
		return Cursor(self.connection.cursor())
		
	def session(self) -> Session:
		return Session(self.connection)

	def commit(self):
		self.connection.commit()
		return

	def rollback(self):
		self.connection.rollback()
		return
