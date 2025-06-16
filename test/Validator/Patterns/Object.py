# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *
from Liquirizia.Validator.Patterns.Object import *
from Liquirizia.Validator.Patterns.String import *

class TestValidatorPatternsObject(Case):

	@Order(1)
	def testIsRequiredIn(self):
		va = Validator(IsRequiredIn('name', 'age'))
		ASSERT_IS_EQUAL(va({'name': 'John', 'age': 30}), {'name': 'John', 'age': 30})
		with ASSERT_EXCEPT(ValueError):
			va({'name': 'John'})
		with ASSERT_EXCEPT(ValueError):
			va({'age': 30})
		return
	
	@Order(2)
	def testIsMappingOf(self):
		va = Validator(IsMappingOf({
			'name': IsAlphabet(),
			'age': IsNumeric(),
		}))
		ASSERT_IS_EQUAL(va({'name': 'John', 'age': '30'}), {'name': 'John', 'age': '30'})
		with ASSERT_EXCEPT(ValueError):
			va({'name': 'John123', 'age': '30'})
		with ASSERT_EXCEPT(ValueError):
			va({'name': 'John', 'age': 'thirty'})
		return

	@Order(3)	
	def testIsKeyOf(self):
		va = Validator(IsKeyOf(IsIn('name', 'age')))
		ASSERT_IS_EQUAL(va({'name': 'John', 'age': 30}), {'name': 'John', 'age': 30})
		ASSERT_IS_EQUAL(va({'name': 'John'}), {'name': 'John'})
		ASSERT_IS_EQUAL(va({'age': 30}), {'age': 30})
		with ASSERT_EXCEPT(ValueError):
			va({'name': 'John', 'age': 30, 'gender': 1})
		return
	
	@Order(4)
	def testIsValueOf(self):
		va = Validator(IsValueOf(IsIn('John', 30)))
		ASSERT_IS_EQUAL(va({'name': 'John', 'age': 30}), {'name': 'John', 'age': 30})
		with ASSERT_EXCEPT(ValueError):
			va({'name': 'Doe', 'age': 30})
		with ASSERT_EXCEPT(ValueError):
			va({'name': 'John', 'age': 25})
		return

