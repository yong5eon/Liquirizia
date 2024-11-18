# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject.Properties.Database import Executors
from Liquirizia.DataModel import Model

from ..Table import Table
from ..View import View

from ..Constraints import Unique

from typing import Type

__all__ = (
	'Drop'
)


class Drop(Executors):
	def __init__(self, o: Type[Model], exist: bool = True):
		self.executors = []
		if issubclass(o, Table):
			for constraint in o.__constraints__ if o.__constraints__ else []:
				if not isinstance(constraint, Unique): continue
				self.executors.append(('DROP INDEX {}{}'.format(
					'IF EXISTS ' if exist else '',
					constraint.name,
				), ()))
			for index in o.__indexes__ if o.__indexes__ else []:
				self.executors.append(('DROP INDEX {}{}'.format(
					'IF EXISTS ' if exist else '',
					index.name,
				), ()))
			self.executors.append(('DROP TABLE {}{}'.format(
				'IF EXISTS ' if exist else '',
				o.__model__,
			), ()))
		if issubclass(o, View):
			self.executors.append(('DROP VIEW {}{}'.format(
				'IF EXISTS ' if exist else '',
				o.__model__,
			), ()))
		return
	
	def __iter__(self):
		return self.executors.__iter__()

