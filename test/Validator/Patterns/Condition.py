# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *

class TestValidatorPatternsCondition(Case):

	@Order(1)
	def testAll(self):
		va = Validator(All(IsIn(1, 2, 3), IsGreaterThan(0)))
		ASSERT_IS_EQUAL(va(1), 1)
		ASSERT_IS_EQUAL(va(2), 2)
		ASSERT_IS_EQUAL(va(3), 3)
		with ASSERT_EXCEPT(ValueError):
			va(0)
		with ASSERT_EXCEPT(ValueError):
			va(4)
		with ASSERT_EXCEPT(ValueError):
			va(-1)
		return

	@Order(2)
	def testAny(self):
		va = Validator(Any(IsIn(1, 2, 3), IsGreaterThan(0)))
		ASSERT_IS_EQUAL(va(1), 1)
		ASSERT_IS_EQUAL(va(2), 2)
		ASSERT_IS_EQUAL(va(3), 3)
		ASSERT_IS_EQUAL(va(4), 4)
		ASSERT_IS_EQUAL(va(5), 5)
		with ASSERT_EXCEPT(ValueError):
			va(0)
		with ASSERT_EXCEPT(ValueError):
			va(-1)
		return
