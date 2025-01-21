# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject.Properties.Database import (
	Session as BaseSession,
	Run,
	Fetch,
	Executor,
	Executors,
	Mapper,
	Filter,
)
from Liquirizia.DataModel import Model

from .Context import Context
from .Cursor import Cursor

from sqlite3 import Connection as SqliteConnection

from typing import Union, Type

__all__ = (
	'Session'
)


class Session(BaseSession, Run):
	"""Session Interface for Database"""

	def __init__(self, connection: SqliteConnection) -> None:
		self.connnection = connection
		self.cursor = self.connnection.cursor()
		return
	
	def __del__(self) -> None:
		self.cursor.close()
		self.connnection.commit()
		return
	
	def execute(self, sql, *args):
		self.cursor.execute(sql, args)
		return Context(self.cursor)
	
	def executes(self, sql, *args):
		self.cursor.executemany(sql, args)
		return Context(self.cursor)

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
		def exec(exec: Executor, cb: callable = None):
			cursor.execute(executor.query, executor.args)
			if not isinstance(exec, Fetch): return
			return exec.fetch(Cursor(cursor), mapper=mapper, filter=filter, fetch=fetch)
		if isinstance(executor, Executors): return execs(executor)
		if isinstance(executor, Executor): return exec(executor)
		raise RuntimeError('{} must be executor or executors'.format(executor.__class__.__name__))
		
	def rows(self):
		def transform(rows):
			li = []  # the dictionary to be filled with the row data and to be returned
			for i, row in enumerate(rows):  # iterate throw the sqlite3.Row objects
				li.append(dict(row))
			return li
		return transform(self.cursor.fetchall())

	def row(self):
		return dict(self.cursor.fetchone())
	
	def count(self):
		raise RuntimeError('Sqlite is not support row count')
