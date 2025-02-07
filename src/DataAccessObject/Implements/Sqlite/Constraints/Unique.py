# -*- coding: utf-8 -*-

from ..Constraint import Constraint

from typing import Union, Sequence

__all__ = (
	'Unique'
)


class Unique(Constraint):
	def __init__(
		self, 
		name: str,
		colexprs: Union[str, Sequence[str]],
		expr: str = None,
		notexists: bool = None,
	):
		self.name = name
		self.table = None
		self.colexprs = colexprs if isinstance(colexprs, (tuple, list)) else [colexprs]
		self.expr = expr
		self.notexists = notexists 
		return
	