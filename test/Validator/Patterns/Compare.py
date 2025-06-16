# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *

class TestValidatorPatternsCompare(Case):

	@Order(1)
	def testIsIn(self):
		va = Validator(IsIn(1, 2, 3))
		ASSERT_IS_EQUAL(va(1), 1)
		ASSERT_IS_EQUAL(va(2), 2)
		ASSERT_IS_EQUAL(va(3), 3)
		with ASSERT_EXCEPT(ValueError):
			va(4)
		return

	@Order(2)
	def testIsNotIn(self):
		va = Validator(IsNotIn(1, 2, 3))
		ASSERT_IS_EQUAL(va(4), 4)
		ASSERT_IS_EQUAL(va(5), 5)
		with ASSERT_EXCEPT(ValueError):
			va(1)
		with ASSERT_EXCEPT(ValueError):
			va(2)
		with ASSERT_EXCEPT(ValueError):
			va(3)
		return
	
	@Order(3)
	def testIsEqualTo(self):
		va = Validator(IsEqualTo(42))
		ASSERT_IS_EQUAL(va(42), 42)
		with ASSERT_EXCEPT(ValueError):
			va(41)
		with ASSERT_EXCEPT(ValueError):
			va(43)
		return
	
	@Order(4)
	def testIsNotEqualTo(self):
		va = Validator(IsNotEqualTo(42))
		ASSERT_IS_EQUAL(va(41), 41)
		ASSERT_IS_EQUAL(va(43), 43)
		with ASSERT_EXCEPT(ValueError):
			va(42)
		return

	@Order(5)
	def testIsGreaterThan(self):
		va = Validator(IsGreaterThan(42))
		ASSERT_IS_EQUAL(va(43), 43)
		ASSERT_IS_EQUAL(va(100), 100)
		with ASSERT_EXCEPT(ValueError):
			va(42)
		with ASSERT_EXCEPT(ValueError):
			va(41)
		return
	
	@Order(6)
	def testIsGreaterEqualTo(self):
		va = Validator(IsGreaterEqualTo(42))
		ASSERT_IS_EQUAL(va(42), 42)
		ASSERT_IS_EQUAL(va(43), 43)
		ASSERT_IS_EQUAL(va(100), 100)
		with ASSERT_EXCEPT(ValueError):
			va(41)
		return
	
	@Order(7)
	def testIsLessThan(self):
		va = Validator(IsLessThan(42))
		ASSERT_IS_EQUAL(va(41), 41)
		ASSERT_IS_EQUAL(va(0), 0)
		with ASSERT_EXCEPT(ValueError):
			va(42)
		with ASSERT_EXCEPT(ValueError):
			va(43)
		return
	
	@Order(8)
	def testIsLessEqualTo(self):
		va = Validator(IsLessEqualTo(42))
		ASSERT_IS_EQUAL(va(42), 42)
		ASSERT_IS_EQUAL(va(41), 41)
		ASSERT_IS_EQUAL(va(0), 0)
		with ASSERT_EXCEPT(ValueError):
			va(43)
		return
