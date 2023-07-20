# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Case import Case

from operator import eq

__all__ = (
	'IsEqualTo'
)


class IsEqualTo(Pattern):
	def __init__(self, condition):
		self.condition = condition
		return
	def __call__(self, case):
		return eq(case(), self.condition)
	def __str__(self):
		return 'is equal to {}'.format(self.condition)
