# -*- coding: utf-8 -*-

from ..Expr import Expr
from ...Type import Type

__all__ = (
	'IsNull',
	'IsNotNull',
)


class IsNull(Expr):
	def __init__(self, col: Type):
		self.col = col
		return
	def __str__(self):
		return '{} IS NULL'.format(
			str(self.col),
		)


class IsNotNull(Expr):
	def __init__(self, col: Type):
		self.col = col
		return
	def __str__(self):
		return '{} IS NOT NULL'.format(
			str(self.col),
		)
