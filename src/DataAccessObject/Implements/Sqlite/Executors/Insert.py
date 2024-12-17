# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject.Properties.Database import (
	Executor,
	Fetch,
	Mapper,
	Filter
)

from ..Table import Table

from typing import Type

__all__ = (
	'Insert'
)


class Insert(Executor, Fetch):
	def __init__(self, o: Type[Table]):
		self.obj = o
		self.table = o.__model__
		self.kwargs = {}
		return
	
	def values(self, **kwargs):
		for k, v in self.obj.__mapper__.items():
			if k not in kwargs.keys(): continue
			self.kwargs[v.key] = v.validator(kwargs[k])
		return self
	
	@property
	def query(self):
		return 'INSERT INTO {}({}) VALUES({}) RETURNING *'.format(
			self.table,
			', '.join(self.kwargs.keys()),
			', '.join(['?' for k in self.kwargs.keys()])
		)

	@property	
	def args(self):
		return list(self.kwargs.values())

	def fetch(self, cursor, mapper: Mapper = None, filter: Filter = None):
		row = dict(cursor.row())
		if mapper: row = {mapper(k): v for k, v in row.items()}
		if filter: row = filter(row)
		obj = self.obj(**row)
		obj.__cursor__ = cursor
		return obj
