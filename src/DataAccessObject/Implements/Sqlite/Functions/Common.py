# -*- coding: utf-8 -*-

from ..Function import Function
from ..Type import Type

__all__ = (
	'Count',
	'Sum',
	'Average',
)


class Count(Function):
	def __init__(self, col: Type):
		self.col = col
		return
	def __str__(self):
		return 'COUNT({})'.format(str(self.col))
	

class Sum(Function):
	def __init__(self, col: Type):
		self.col = col
		return
	def __str__(self):
		return 'SUM({})'.format(str(self.col))


class Average(Function):
	def __init__(self, col: Type):
		self.col = col
		return
	def __str__(self):
		return 'AVG({})'.format(str(self.col))
