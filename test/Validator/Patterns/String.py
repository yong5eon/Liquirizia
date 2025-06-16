# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns.String import *

class TestValidatorPatternsString(Case):

	@Order(1)
	def testIsAlphabet(self):
		va = Validator(IsAlphabet())
		ASSERT_IS_EQUAL(va('abc'), 'abc')
		ASSERT_IS_EQUAL(va('ABC'), 'ABC')
		with ASSERT_EXCEPT(ValueError):
			va('abc123')
		with ASSERT_EXCEPT(ValueError):
			va('123')
		return
	
	@Order(2)
	def testIsAlphaNumeric(self):
		va = Validator(IsAlphaNumeric())
		ASSERT_IS_EQUAL(va('abc123'), 'abc123')
		ASSERT_IS_EQUAL(va('ABC123'), 'ABC123')
		with ASSERT_EXCEPT(ValueError):
			va('abc 123')
		with ASSERT_EXCEPT(ValueError):
			va('abc!')
		return
	
	@Order(3)
	def testIsNumeric(self):
		va = Validator(IsNumeric())
		ASSERT_IS_EQUAL(va('123'), '123')
		ASSERT_IS_EQUAL(va('456'), '456')
		with ASSERT_EXCEPT(ValueError):
			va('123abc')
		with ASSERT_EXCEPT(ValueError):
			va('abc')
		return
	
	@Order(4)
	def testToUpper(self):
		va = Validator(ToUpper())
		ASSERT_IS_EQUAL(va('abc'), 'ABC')
		ASSERT_IS_EQUAL(va('ABC'), 'ABC')
		ASSERT_IS_EQUAL(va('123abc'), '123ABC')
		return
	
	@Order(5)
	def testToLower(self):
		va = Validator(ToLower())
		ASSERT_IS_EQUAL(va('ABC'), 'abc')
		ASSERT_IS_EQUAL(va('abc'), 'abc')
		ASSERT_IS_EQUAL(va('123ABC'), '123abc')
		return
	
	@Order(6)
	def testIsSubString(self):
		va = Validator(IsSubString('abc'))
		ASSERT_IS_EQUAL(va('abc123'), 'abc123')
		with ASSERT_EXCEPT(ValueError):
			va('xyzabc')
		with ASSERT_EXCEPT(ValueError):
			va('123abc')
		with ASSERT_EXCEPT(ValueError):
			va('xyz')
		with ASSERT_EXCEPT(ValueError):
			va('123')
		return
