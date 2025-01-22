# -*- coding: utf-8 -*-

from .Join import Join

from ..Table import Table

from typing import Type

__all__ = (
	'RightOuter'
)


class RightOuter(Join):
	"""Right Outer Join Class"""

	def __init__(self, table: Type[Table], *args) -> None:
		super(RightOuter, self).__init__('RIGHT OUTER', table, *args)
		return
