# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton
from .Timer import Timer

from collections.abc import Iterable, Mapping

__all__ = (
	'DurationTimer',
	'Duration',
)


class DurationTimer(Mapping, Iterable, Singleton):
	'''Duration Timer Class'''

	def __init__(self) -> None:
		self.__table__ = {}
		return

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.__table__.__repr__()[1:-1]
		)

	def __str__(self): return self.__table__.__str__()

	def __iter__(self): return self.__table__.__iter__()

	def __getitem__(self, key): return self.__table__.__getitem__(key)
	def __len__(self): return self.__table__.__len__()
	def __copy__(self): return self
	def __deepcopy__(self): return self

	def add(self, name, timer : Timer):
		if name not in self.__table__.keys():
			self.__table__[name] = []
		self.__table__[name].append(timer)
		return

	def min(self, name: str = None):
		if name:
			if name not in self.__table__.keys():
				return 0
			return min(self.__table__[name])
		_ = [v for k, v in self.__table__.items()]
		return min(_)

	def max(self, name: str = None):
		if name:
			if name not in self.__table__.keys():
				return 0
			return max(self.__table__[name])
		_ = [v for k, v in self.__table__.items()]
		return max(_)

	def sum(self, name: str = None):
		if name:
			if name not in self.__table__.keys():
				return 0
			return sum([t.duration for t in self.__table__[name]])
		_ = []
		for k, v in self.__table__.items():
			__ = [t.duration for t in v]
			_.extend(__)
		return sum(_)

	def count(self, name: str = None):
		if name:
			if name not in self.__table__.keys():
				return 0
			return len(self.__table__[name])
		_ = []
		for k, v in self.__table__.items():
			__ = [t.duration for t in v]
			_.extend(__)
		return len(_)

	def avg(self, name: str = None):
		return self.sum(name)/self.count(name)
