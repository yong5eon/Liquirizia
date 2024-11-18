# -*- coding: utf-8 -*-

from ..Function import Function
from ..Type import Type

__all__ = (
	'IfNull'
)


class IfNull(Function):
	def __init__(self, attr: Type, value: any):
		self.attr = attr
		self.value = value
		return
	def __str__(self):
		return 'IFNULL({}, {})'.format(
			str(self.attr),
			self.value,
		)