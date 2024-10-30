# -*- coding: utf-8 -*-

from .Order import OrderContext

from unittest import TestCase, TestLoader, TestSuite

from os.path import splitext, split
from pathlib import Path
from importlib.machinery import SourceFileLoader
from inspect import getmembers, isclass

from typing import Type, Sequence

__all__ = (
	'Loader'
)


class Loader(TestLoader):
	def getTestCaseNames(self, testCaseClass: Type[TestCase]) -> Sequence[str]:
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
	
	def file(self, path):
		head, tail = split(path)
		file, ext = splitext(tail)
		head = head.replace('\\', '.').replace('/', '.')
		mod = '{}.{}'.format(head, file)
		loader = SourceFileLoader(mod, path)
		mo = loader.load_module()
		if not mo:
			return None
		return self.loadTestsFromModule(mo)
