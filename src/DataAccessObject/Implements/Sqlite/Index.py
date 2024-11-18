# -*- coding: utf-8 -*-

from typing import Sequence, Union

__all__ = (
	'Index'
)


class Index(object):
	def __init__(
		self, 
		name: str,
		colexprs: Union[str, Sequence[str]],
		expr: str = None,
		notexists: bool = True,
	):
		self.name = name
		self.colexprs = colexprs if isinstance(colexprs, (tuple, list)) else [colexprs]
		self.expr = expr
		self.notexists = notexists
		return
	