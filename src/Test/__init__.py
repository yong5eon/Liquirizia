# -*- coding: utf-8 -*-

from .Runner import Runner
from .Case import Case
from .Fixture import Fixture
from .Pattern import Pattern

from abc import (
	ABC,
	ABCMeta,
)

__all__ = (
	'Runner',
	'Case',
	'Fixture',
	'Pattern',
	'ASSERT',
)


class AssertCase(Case):
	def __init__(self, expr, description: str = None):
		self.case = expr 
		self.description = description
		return
	def __call__(self):
		return self.case
	def __str__(self):
		return str(self.case) if not self.description else self.description


def ASSERT(case: Case, pattern: Pattern, setup: Fixture = None, teardown: Fixture = None, description: str = None):
	_ = Runner()
	_.add(case if isinstance(case, Case) else AssertCase(case, description=description), pattern, setup, teardown)
	# _.test(case if isinstance(case, Case) else AssertCase(case, description=description), pattern, setup, teardown)
	return
