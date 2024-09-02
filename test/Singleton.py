# -*- coding: utf-8 -*-

from Liquirizia.Test import *
from Liquirizia.Template import Singleton

from sys import stderr
from copy import copy, deepcopy


class SampleObject(Singleton):

	def __init__(self, const=None):
		self.const = const if const else 0
		self.x = 0
		return
	
	def set(self, x):
		self.x = self.const + x

	def get(self):
		return self.x


class TestSingleton(Case):
	def __init__(self, methodName: str = "runTest") -> None:
		super().__init__(methodName)
		return
	
	@classmethod
	def setUpClass(cls) -> None:
		cls._ = SampleObject(0)
		return super().setUpClass()


	@Parameterized(
			{'v': 1},
			{'v': 2},
			{'v': 3},
	)
	@Order(0)
	def testCreate(self, v):
		with ASSERT_EXCEPT(RuntimeError) as e:
			o = SampleObject(v)
			ASSERT_IS_EQUAL(e.exception, RuntimeError)
			ASSERT_IS_EQUAL(id(o), id(_))
		return

	@Parameterized(
			{'v': 1},
			{'v': 2},
			{'v': 3},
	)
	@Order(1)
	def testSet(self, v):
		o = SampleObject()
		o.set(v)
		ASSERT_IS_EQUAL(self.__class__._.get(), o.get())

	@Parameterized(
			{'v': 1},
			{'v': 2},
			{'v': 3},
	)
	@Order(2)
	def testCopy(self, v):
		ASSERT_IS_EQUAL(id(self.__class__._), id(copy(self.__class__._)))
		ASSERT_IS_EQUAL(id(self.__class__._), id(deepcopy(self.__class__._)))
