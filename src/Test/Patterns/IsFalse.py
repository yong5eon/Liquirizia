# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Case import Case

from operator import eq

__all__ = (
	'IsFalse'
)


class IsFalse(Pattern):
	def __init__(self):
		self.condition = False 
		return
	def __call__(self, case):
		return bool(case()) is self.condition
	def __str__(self):
		return 'is {}'.format(self.condition)
