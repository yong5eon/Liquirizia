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

from typing import Optional, Annotated


class TestDataModelWithTuple(Case):

	@Order(1)
	def testValue(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=tuple,
				va=Validator(IsTuple()),
			)
		_ = TestModel(val=(1,2,3))
		ASSERT_IS_EQUAL(_.val, (1,2,3))
		_.val = ()
		ASSERT_IS_EQUAL(_.val, ())
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
				type=tuple,
				va=Validator(IsTuple()),
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_.val = (1, 2, 3)
		ASSERT_IS_EQUAL(_.val, (1, 2, 3))
		_.val = ()
		ASSERT_IS_EQUAL(_.val, ())
		_.val = None
		ASSERT_IS_EQUAL(_.val, None)
		class TestModel(
			Model,
		):
			val = Value(
				type=tuple,
				va=Validator(IsTuple()),
				default=(),
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, ())
		_.val = (1, 2, 3)
		ASSERT_IS_EQUAL(_.val, (1, 2, 3))
		with ASSERT_EXCEPT(ValueError):
			_.val = None
		return
	
	@Order(3)
	def testValueWithDetectChangedElement(self):
		class TestHandler(
			Handler,
		):
			def __call__(self, o: 'TestModel', p: Value, v: tuple, pv: tuple):
				o.pval = pv
				return 
		class TestModel(
			Model,
		):
			val = Value(
				type=tuple,
				va=Validator(IsTuple()),
				fn=TestHandler(),
				default=(),
			)
			pval = Value(
				type=tuple,
				va=Validator(IsTuple()),
				default=None,
			)
		_ = TestModel()
		_.val = (1, 2, 3)
		ASSERT_IS_EQUAL(_.val, (1,2,3))
		ASSERT_IS_EQUAL(_.pval, ())
		return
