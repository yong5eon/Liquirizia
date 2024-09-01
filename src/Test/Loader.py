# -*- coding: utf-8 -*-

from ..Template import Singleton

from .Order import OrderContext

from collections.abc import Sequence
from unittest import TestCase, TestLoader

__all__ = (
	'Loader'
)


class Loader(TestLoader):
	def getTestCaseNames(self, testCaseClass: type[TestCase]) -> Sequence[str]:
		context = OrderContext()
		cases = super().getTestCaseNames(testCaseClass)
		orderedCases = context.get(testCaseClass.__name__)
		if not orderedCases:
			return cases
		_ = []
		for case in cases:
			if case not in orderedCases.keys():
				_.append((case, 0))
			else:
				_.append((case, orderedCases[case]))
		_.sort(key=lambda o: o[1])
		return [m for m, order in _]