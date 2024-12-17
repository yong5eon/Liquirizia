# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject.Properties.Database import (
	Cursor as BaseCursor,
	Executors,
	Executor,
	Fetch,
	Run,
	Mapper,
	Filter,
)

from .Context import Context

from sqlite3 import Cursor as SqliteCuror

from typing import Union

__all__ = (
	'Cursor'
)


class Cursor(BaseCursor, Run):
	"""Cursor for Sqlite"""
	def __init__(self, cursor: SqliteCuror):
		self.cursor = cursor
		return

	def execute(self, sql, *args) -> Context:
		self.cursor.execute(sql, args)
		return Context(self.cursor)
	
	def executes(self, sql, *args) -> Context:
		self.cursor.execute(sql, args)
		return Context(self.cursor)
	
	def run(self, executor: Union[Executor,Executors], mapper: Mapper = None, filter: Filter = None):
		def execs(execs: Executors):
			__ = []
			for query, args in execs:
				self.cursor.execute(query, args)
				if not isinstance(executor, Fetch): continue
				rows = executor.fetch(Cursor(self.cursor), mapper=mapper, filter=filter)
				__.extend(rows)
			return __
		def exec(exec: Executor):
			self.cursor.execute(exec.query, exec.args)
			if not isinstance(exec, Fetch): return
			return exec.fetch(Cursor(self.cursor), mapper=mapper, filter=filter)
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
		return RuntimeError('Sqlite is not support row count')
