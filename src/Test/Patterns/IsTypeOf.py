# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Case import Case

from operator import eq

__all__ = (
	'IsTypeOf'
)


class IsTypeOf(Pattern):
	def __init__(self, condition):
		self.condition = condition
		return
	def __call__(self, case: Case):
		return isinstance(case(), self.condition)
	def __str__(self):
		return 'is type of {}'.format(self.condition.__name__)
