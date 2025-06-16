# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validate, Validator, Pattern

class TestValidator(Case):

	@Parameterized(
			{'input': 2, 'success': 2, 'fail': 3},
	)
	@Order(1)	
	def testPattern(self, input, success, fail):
		class TestPattern(Pattern):
			def __init__(self, success):
				self.success = success
				return
			def __call__(self, parameter):
				if parameter == self.success:
					return parameter + self.success
				raise ValueError('{} is not equal to {}'.format(parameter, self.success))
		va = Validator(TestPattern(success))
		ASSERT_IS_EQUAL(va(input), input + success)
		with ASSERT_EXCEPT(ValueError):
			fail = va(fail)
		return
