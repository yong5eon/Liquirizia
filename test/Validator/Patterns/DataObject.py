# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *
from Liquirizia.Validator.Patterns.DataObject import *
from Liquirizia.Validator.Patterns.String import *

from dataclasses import dataclass

@dataclass
class Person:
	name: str
	age: int

@dataclass
class Employee:
	name: str
	title: str

class TestValidatorPatternsDataObject(Case):

	@Order(1)
	def testIsRequiredIn(self):
		va = Validator(IsRequiredIn('name', 'age'))
		ASSERT_IS_EQUAL(va(Person(name='John', age=30)), Person(name='John', age=30))
		with ASSERT_EXCEPT(ValueError):
			va(Employee(name='John', title='Manager'))
		return
	
	@Order(2)
	def testIsMappingOf(self):
		va = Validator(IsMappingOf({
			'name': IsAlphabet(),
			'age': IsInteger(),
		}))
		ASSERT_IS_EQUAL(va(Person(name='John', age=30)), Person(name='John', age=30))
		with ASSERT_EXCEPT(TypeError):
			va(Person(name='John', age='thirty'))
		with ASSERT_EXCEPT(ValueError):
			va(Employee(name='John123', title='Manager'))
		return
