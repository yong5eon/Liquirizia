# -*- coding: utf-8 -*-

from Liquirizia.Test import *
from Liquirizia.DataModel import (
	Model,
	Value, 
	Handler,
)
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *
from Liquirizia.Validator.Patterns.Array import *
from dataclasses import dataclass
from typing import Optional, Annotated

@dataclass
class TestDataObject:
	a: int
	b: float
	c: str

class TestDataModelWithDataObject(Case):

	@Order(1)
	def testValue(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=TestDataObject,
				va=Validator(IsDataObject()),
			)
		_ = TestModel(val=TestDataObject(a=1, b=2.0, c='3'))
		ASSERT_IS_EQUAL(_.val, TestDataObject(a=1, b=2.0, c='3'))
		_.val.a = 2
		ASSERT_IS_EQUAL(_.val, TestDataObject(a=2, b=2.0, c='3'))
		with ASSERT_EXCEPT(TypeError):
			_.val = TestDataObject()
		with ASSERT_EXCEPT(ValueError):
			_ = TestModel()
		with ASSERT_EXCEPT(ValueError):
			_ = TestModel(val=None)
		return
	
	@Order(2)
	def testValueWithDefault(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=TestDataObject,
				va=Validator(IsDataObject()),
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_.val = TestDataObject(a=1, b=2.0, c='3')
		ASSERT_IS_EQUAL(_.val, TestDataObject(a=1, b=2.0, c='3'))
		_.val.a = 2
		ASSERT_IS_EQUAL(_.val, TestDataObject(a=2, b=2.0, c='3'))
		_.val = None
		ASSERT_IS_EQUAL(_.val, None)
		with ASSERT_EXCEPT(TypeError):
			_.val = TestDataObject()
		class TestModel(
			Model,
		):
			val = Value(
				type=dict,
				va=Validator(IsDataObject()),
				default=TestDataObject(a=1, b=2.0, c='3'),
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, TestDataObject(a=1, b=2.0, c='3'))
		_.val = TestDataObject(a=2, b=3.0, c='4')
		ASSERT_IS_EQUAL(_.val, TestDataObject(a=2, b=3.0, c='4'))
		with ASSERT_EXCEPT(ValueError):
			_.val = None
		return

	@Order(3)
	def testValueWithDetectChangedElement(self):
		class TestHandler(
			Handler,
		):
			def __call__(self, o: 'TestModel', p: Value, v: dict, pv: dict):
				o.pval = pv
				return
		class TestModel(
			Model,
		):
			val = Value(
				type=TestDataObject,
				va=Validator(IsDataObject()),
				fn=TestHandler(),
				default=TestDataObject(a=0, b=0.0, c=''),
			)
			pval = Value(
				type=TestDataObject,
				va=Validator(IsDataObject()),
				default=None,
			)
		_ = TestModel()
		_.val.a = 1
		ASSERT_IS_EQUAL(_.val, TestDataObject(a=1, b=0.0, c=''))
		ASSERT_IS_EQUAL(_.pval, TestDataObject(a=0, b=0.0, c=''))
		_.val.b = 2.0
		ASSERT_IS_EQUAL(_.val, TestDataObject(a=1, b=2.0, c=''))
		ASSERT_IS_EQUAL(_.pval, TestDataObject(a=1, b=0.0, c=''))
		_.val.c = '3'
		ASSERT_IS_EQUAL(_.val, TestDataObject(a=1, b=2.0, c='3'))
		ASSERT_IS_EQUAL(_.pval, TestDataObject(a=1, b=2.0, c=''))
		_.val = TestDataObject(a=0, b=0.0, c='')
		ASSERT_IS_EQUAL(_.val, TestDataObject(a=0, b=0.0, c=''))
		ASSERT_IS_EQUAL(_.pval, TestDataObject(a=1, b=2.0, c='3'))
		return