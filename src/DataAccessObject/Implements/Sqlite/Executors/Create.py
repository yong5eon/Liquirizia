# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject.Properties.Database import Executors
from Liquirizia.DataModel import Model

from ..Table import Table
from ..View import View
from ..Type import Type
from ..Index import Index

from ..Constraints import (
	PrimaryKey,
	ForeignKey,
	Unique,
)

from typing import Type as T

__all__ = (
	'Create'
)


class TypeToSQL(object):
	def __call__(self, col: Type) -> str:
		return '{} {}{}{}'.format(
			col.key,
			col.type,
			' NOT NULL' if not col.null else '',
			' DEFAULT {}'.format(col.default) if col.default else '',
		)

class PrimaryKeyToSQL(object):
	def __call__(self, key: PrimaryKey) -> str:
		return 'PRIMARY KEY({}{})'.format(
			', '.join(key.cols),
			' AUTOINCREMENT' if key.autoincrement else '',
		)

class ForeignKeyToSQL(object):
	def __call__(self, key: ForeignKey) -> str:
		return 'FOREIGN KEY({}) REFERENCES {}({})'.format(
			', '.join(key.cols),
			key.reference,
			', '.join(key.referenceCols)
		)

class UniqueToSQL(object):
	def __call__(self, o: T[Table], index: Unique) -> str:
		return 'CREATE UNIQUE INDEX {}{} ON {}({}){}'.format(
			'IF NOT EXISTS ' if index.notexists else '',
			index.name,
			o.__model__,
			', '.join(index.colexprs),
			' WHERE {}'.format(index.expr) if index.expr else '',
		)

class IndexToSQL(object):
	def __call__(self, o: T[Table], index: Index) -> str:
		return 'CREATE INDEX {}{} ON {}({}){}'.format(
			'IF NOT EXISTS ' if index.notexists else '',
			index.name,
			o.__model__,
			', '.join(index.colexprs),
			' WHERE {}'.format(index.expr) if index.expr else '',
		)


class TableToSQL(object):

	TypeToSQL = TypeToSQL()
	PrimaryKeyToSQL = PrimaryKeyToSQL()
	ForeignKeyToSQL = ForeignKeyToSQL()
	UniqueToSQL = UniqueToSQL()
	IndexToSQL = IndexToSQL()

	def __call__(self, o: T[Table], notexist) -> str:
		__ = []
		_ = []
		for k, v in o.__mapper__.items():
			_.append(self.TypeToSQL(v))
		for constraint in o.__constraints__ if o.__constraints__ else []:
			if isinstance(constraint, PrimaryKey):
				_.append(self.PrimaryKeyToSQL(constraint))
				continue
			if isinstance(constraint, ForeignKey):
				_.append(self.ForeignKeyToSQL(constraint))
		__.append(('CREATE TABLE {}{}({})'.format(
			'IF NOT EXISTS ' if notexist else '',
			o.__model__,
			', '.join(_)
		), ()))
		for constraint in o.__constraints__ if o.__constraints__ else []:
			if isinstance(constraint, Unique):
				__.append((self.UniqueToSQL(o, constraint), ()))
				continue
		for index in o.__indexes__ if o.__indexes__ else []:
			if isinstance(index, Index):
				__.append((self.IndexToSQL(o, index), ()))
				continue
		# TODO: CREATE COMMENT
		return __
	

class ViewToSQL(object):
	def __call__(self, o: T[View], notexist) -> str:
		return [('CREATE VIEW {}{} AS {}'.format(
			'IF NOT EXISTS ' if notexist else '',
			o.__model__,
			o.__executor__.query,
		), ())]


class Create(Executors):

	TableToSQL = TableToSQL()
	ViewToSQL = ViewToSQL()

	def __init__(self, o: T[Model], notexist: bool = True):
		self.model = o
		self.executors = []
		if issubclass(o, Table):
			self.executors = self.TableToSQL(o, notexist)
		if issubclass(o, View):
			self.executors = self.ViewToSQL(o, notexist)
		return
	
	def __iter__(self):
		return self.executors.__iter__()
	