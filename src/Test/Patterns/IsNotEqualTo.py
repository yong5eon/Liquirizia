# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Case import Case

from operator import ne

__all__ = (
	'IsNotEqualTo'
)


class IsNotEqualTo(Pattern):
	def __init__(self, condition):
		self.condition = condition
		return
	def __call__(self, case):
		return ne(case(), self.condition)
	def __str__(self):
		return 'is not equal to {}'.format(self.condition)
