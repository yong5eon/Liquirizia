# -*- coding: utf-8 -*-

from ..Expr import Expr

from ...Type import Type

__all__ = (
	'Ascend'
)


class Ascend(Expr):
	"""Ascend Order Class"""

	def __init__(self, col: Type, null='LAST') -> None:
		self.col = col
		self.null = null
		return

	def __str__(self):
		return '{} ASC{}'.format(
			str(self.col) if isinstance(self.col, Type) else self.col,
			' NULLS {}'.format(self.null) if self.null else '',
		)