# -*- coding: utf-8 -*-

from Liquirizia.DataModel import Model, Handler
from Liquirizia.DataModel.Format import Object


from .Index import Index
from .Constraint import Constraint

from typing import Sequence


__all__ = (
	'Table'
)


class Table(Model):
	"""Table Model Class"""
	def __new__(cls, **kwargs):
		o = super().__new__(cls, **kwargs)
		o.__cursor__ = None
		return o

	def __init__(self, **kwargs):
		_ = {}
		for k, v in kwargs.items():
			for c, t in self.__mapper__.items():
				if k == t.key:
					k = c
			_[k] = v
		return super().__init__(**_)

	def __setattr__(self, name, value):
		if name in ('__cursor__'): return super(Model, self).__setattr__(name, value)
		return super().__setattr__(name, value)

	def __init_subclass__(
		cls,
		name: str = None,
		constraints: Sequence[Constraint] = None,
		indexes: Sequence[Index] = None,
		description: str = None,
		schema: Object = None,
		fn: Handler = None,
	):
		cls.__model__ = name if name else cls.__name__
		if constraints:
			if isinstance(constraints, Constraint): constraints = [constraints]
		cls.__constraints__ = constraints
		if indexes:
			if isinstance(indexes, Index): indexes = [indexes]
		cls.__indexes__ = indexes
		return super().__init_subclass__(description, schema, fn)
