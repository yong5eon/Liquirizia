# -*- coding: utf-8 -*-

from typing import Type
from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *
from Liquirizia.Validator.Patterns.Array import *

class TestValidatorPatternsArray(Case):

	@Order(1)
	def testIsElementOf(self):
		va = Validator(IsArray(IsElementOf(IsIn('apple', 'banana', 'cherry'))))
		ASSERT_IS_EQUAL(va(['apple']), ['apple'])
		ASSERT_IS_EQUAL(va(['banana', 'cherry']), ['banana', 'cherry'])
		with ASSERT_EXCEPT(ValueError):
			va(['apple', 'orange'])
		with ASSERT_EXCEPT(ValueError):
			va(['kiwi'])
		with ASSERT_EXCEPT(ValueError):
			va('apple')
		with ASSERT_EXCEPT(TypeError):
			va(123)
		with ASSERT_EXCEPT(TypeError):
			va(None)
		with ASSERT_EXCEPT(ValueError):
			va({'fruit': 'apple'})
		return
