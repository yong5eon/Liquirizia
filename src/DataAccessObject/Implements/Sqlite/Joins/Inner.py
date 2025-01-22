# -*- coding: utf-8 -*-

from .Join import Join

from ..Table import Table

from typing import Type

__all__ = (
	'Inner'
)


class Inner(Join):
	"""Inner Join Class"""

	def __init__(self, table: Type[Table], *args) -> None:
		super(Inner, self).__init__('INNER', table, *args)
		return
