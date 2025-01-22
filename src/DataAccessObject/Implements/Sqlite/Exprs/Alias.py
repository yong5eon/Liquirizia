# -*- coding: utf-8 -*-

from ..Expr import Expr
from ..Type import Type

__all__ = (
	'Alias'
)


class Alias(Expr):
	def __init__(self, col: Type, name: str):
		self.col = col
		self.name = name
		return
	def __str__(self):
		return '{} AS {}'.format(
			str(self.col),
			self.name,
		)