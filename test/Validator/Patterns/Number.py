# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns.Number import *

class TestValidatorPatternsNumber(Case):

	@Order(1)
	def testIsRange(self):
		va = Validator(IsRange(1, 10))
		ASSERT_IS_EQUAL(va(1), 1)
		ASSERT_IS_EQUAL(va(5), 5)
		with ASSERT_EXCEPT(ValueError):
			va(0)
		with ASSERT_EXCEPT(ValueError):
			va(10)
		return
