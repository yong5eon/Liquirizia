# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject.Properties.Database import (
	Cursor as BaseCursor,
	Executors,
	Executor,
	Fetch,
	Run,
)

from Liquirizia.DataAccessObject import Error
from Liquirizia.DataAccessObject.Errors import *
from Liquirizia.DataAccessObject.Properties.Database.Errors import *

from .Context import Context

from sqlite3 import Cursor as SqliteCuror
from sqlite3 import DatabaseError, IntegrityError, ProgrammingError, OperationalError, NotSupportedError

from typing import Union

__all__ = (
	'Cursor'
)


class Cursor(BaseCursor):
	"""Cursor for Sqlite"""
	def __init__(self, cursor: SqliteCuror):
		self.cursor = cursor
		return

	def execute(self, sql, *args) -> Context:
		try:
			self.cursor.execute(sql, args)
			return Context(self.cursor)
		except (DatabaseError, IntegrityError, ProgrammingError, NotSupportedError) as e:
			raise ExecuteError(str(e), error=e)
		except OperationalError as e:
			raise ConnectionClosedError(error=e)
		except Exception as e:
			raise Error(str(e), error=e)
		return
	
	def executes(self, sql, *args) -> Context:
		try:
			self.cursor.execute(sql, args)
			return Context(self.cursor)
		except (DatabaseError, IntegrityError, ProgrammingError, NotSupportedError) as e:
			raise ExecuteError(str(e), error=e)
		except OperationalError as e:
			raise ConnectionClosedError(error=e)
		except Exception as e:
			raise Error(str(e), error=e)
	
	def run(self, executor: Union[Executor,Executors]):
		try:
			def execs(execs: Executors):
				__ = []
				for query, args in execs:
					self.cursor.execute(query, args)
					if not isinstance(executor, Fetch): continue
					rows = executor.fetch(Cursor(self.cursor))
					__.extend(rows)
				return __
			def exec(exec: Executor):
				self.cursor.execute(exec.query, exec.args)
				if not isinstance(exec, Fetch): return
				return exec.fetch(Cursor(self.cursor))
			if isinstance(executor, Executors): return execs(executor)
			if isinstance(executor, Executor): return exec(executor)
		except (DatabaseError, IntegrityError, ProgrammingError, NotSupportedError) as e:
			raise ExecuteError(str(e), error=e)
		except OperationalError as e:
			raise ConnectionClosedError(error=e)
		except Exception as e:
			raise Error(str(e), error=e)
	
	def rows(self):
		def transform(rows):
			li = []  # the dictionary to be filled with the row data and to be returned
			for i, row in enumerate(rows):  # iterate throw the sqlite3.Row objects
				li.append(dict(row))
			return li
		try:
			return transform(self.cursor.fetchall())
		except (DatabaseError, IntegrityError, ProgrammingError, NotSupportedError) as e:
			raise ExecuteError(str(e))
		except OperationalError as e:
			raise ConnectionError(str(e), error=e)
		except Exception as e:
			raise Error(str(e), error=e)

	def row(self):
		try:
			return dict(self.cursor.fetchone())
		except (DatabaseError, IntegrityError, ProgrammingError, NotSupportedError) as e:
			raise ExecuteError(str(e))
		except OperationalError as e:
			raise ConnectionError(str(e), error=e)
		except Exception as e:
			raise Error(str(e), error=e)

	def count(self):
		return NotSupportedError('Sqlite is not support row count')
