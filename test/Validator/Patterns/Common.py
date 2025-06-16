# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *

class TestValidatorPatternsCommon(Case):

	@Order(1)
	def testSetDefault(self):
		va = Validator(SetDefault(42))
		ASSERT_IS_EQUAL(va(None), 42)
		ASSERT_IS_EQUAL(va(0), 0)
		ASSERT_IS_EQUAL(va(100), 100)
		return
	
	@Order(2)
	def testIsToNone(self):
		va = Validator(IsToNone(SetDefault(42)))
		ASSERT_IS_EQUAL(va(None), None)
		ASSERT_IS_EQUAL(va(0), 0)
		ASSERT_IS_EQUAL(va(100), 100)
		return
	
	@Order(3)
	def testIsNotToNone(self):
		va = Validator(IsNotToNone(SetDefault(42)))
		ASSERT_IS_EQUAL(va(0), 0)
		ASSERT_IS_EQUAL(va(100), 100)
		with ASSERT_EXCEPT(ValueError):
			va(None)
		return
	
	@Order(4)
	def testIsNotEmpty(self):
		va = Validator(IsNotEmpty(SetDefault('Hello World!')))
		ASSERT_IS_EQUAL(va('Hello'), 'Hello')
		ASSERT_IS_EQUAL(va('World'), 'World')
		with ASSERT_EXCEPT(ValueError):
			va('')
		return
