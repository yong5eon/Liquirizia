# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Case import Case

__all__ = (
	'IsAll'
)


class IsAll(Pattern):
	def __init__(self, *args):
		self.patterns = args
		self.cursor = None
		return

	def __call__(self, case: Case):
		for pattern in self.patterns:
			try:
				if pattern(case):
					continue
				else:
					self.cursor = pattern
					return False
			except Exception as e:
				self.cursor = pattern
				raise e
		return True

	def __str__(self):
		if self.cursor:
			return str(self.cursor)
		return ', '.join(str(pattern) for pattern in self.patterns)
