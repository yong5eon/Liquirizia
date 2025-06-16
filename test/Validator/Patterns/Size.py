# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns.Size import *

class TestValidatorPatternsSize(Case):

	@Order(1)
	def testIsSizeOf(self):
		va = Validator(IsSizeOf(3))
		ASSERT_IS_EQUAL(va([1, 2, 3]), [1, 2, 3])
		ASSERT_IS_EQUAL(va('abc'), 'abc')
		with ASSERT_EXCEPT(ValueError):
			va([1, 2])
		with ASSERT_EXCEPT(ValueError):
			va('ab')
		return
	
	@Order(2)
	def testIsSizeIn(self):
		va = Validator(IsSizeIn(4, min=2))
		ASSERT_IS_EQUAL(va([1, 2]), [1, 2])
		ASSERT_IS_EQUAL(va([1, 2, 3, 4]), [1, 2, 3, 4])
		ASSERT_IS_EQUAL(va('ab'), 'ab')
		ASSERT_IS_EQUAL(va('abcd'), 'abcd')
		with ASSERT_EXCEPT(ValueError):
			va([1])
		with ASSERT_EXCEPT(ValueError):
			va([1, 2, 3, 4, 5])
		with ASSERT_EXCEPT(ValueError):
			va('a')
		with ASSERT_EXCEPT(ValueError):
			va('abcde')
		return
	
	@Order(3)
	def testIsMinSizeOf(self):
		va = Validator(IsMinSizeOf(3))
		ASSERT_IS_EQUAL(va([1, 2, 3]), [1, 2, 3])
		ASSERT_IS_EQUAL(va([1, 2, 3, 4]), [1, 2, 3, 4])
		ASSERT_IS_EQUAL(va('abc'), 'abc')
		ASSERT_IS_EQUAL(va('abcd'), 'abcd')
		with ASSERT_EXCEPT(ValueError):
			va([1, 2])
		with ASSERT_EXCEPT(ValueError):
			va('ab')
		return
	
	@Order(4)
	def testIsMaxSizeOf(self):
		va = Validator(IsMaxSizeOf(3))
		ASSERT_IS_EQUAL(va([1, 2, 3]), [1, 2, 3])
		ASSERT_IS_EQUAL(va([1, 2]), [1, 2])
		ASSERT_IS_EQUAL(va('abc'), 'abc')
		ASSERT_IS_EQUAL(va('ab'), 'ab')
		with ASSERT_EXCEPT(ValueError):
			va([1, 2, 3, 4])
		with ASSERT_EXCEPT(ValueError):
			va('abcd')
		return
