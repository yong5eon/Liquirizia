# -*- coding: utf-8 -*-

from ast import Or
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
	def testTupleValue(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=tuple
			)
		_ = TestModel(val=(1,2,3))
		ASSERT_IS_EQUAL(_.val, (1,2,3))
		with ASSERT_EXCEPT(ValueError): _.val = None
		_.val = (1, 2, 3)
		ASSERT_IS_EQUAL(_.val, (1, 2, 3))
		_.val = (1, 2, 3, 3)
		ASSERT_IS_EQUAL(_.val, (1, 2, 3, 3))
		with ASSERT_EXCEPT(ValueError):
			_ = TestModel()
		with ASSERT_EXCEPT(ValueError):
			_ = TestModel(val=None)
		return
	
	@Order(2)
	def testTupleValueWithDefault(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=tuple,
				default=tuple()
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, tuple())
		class TestModel(
			Model,
		):
			val = Value(
				type=tuple,
				default=None
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		return
	
	@Order(3)
	def testTupleValueWithValidator(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=tuple,
				va=Validator(IsTuple(IsElementOf(IsInteger()))),
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_.val = (1, 2, 3)
		ASSERT_IS_EQUAL(_.val, (1, 2, 3))
		_.val = None
		ASSERT_IS_EQUAL(_.val, None)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val=1)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val='True')
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val={1, 2.0, '3'})
		with ASSERT_EXCEPT(TypeError):
			_.val[0] = '1'
		return
	
	@Order(4)
	def testTupleValueWithDetectChangedElement(self):
		class TestHandler(
			Handler,
		):
			def __call__(self, o, p, v, pv):
				o.changed = v
				return
		class TestModel(
			Model,
		):
			val = Value(
				type=tuple,
				va=Validator(IsTuple(IsElementOf(IsInteger()))),
				fn=TestHandler(),
				default=None,
			)
			changed = Value(
				type=tuple,
				va=Validator(IsTuple(IsElementOf(IsInteger()))),
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		with ASSERT_EXCEPT(TypeError): _.val = [1,2,3]
		with ASSERT_EXCEPT(TypeError): _.val = (1,2,3)
		_.val = tuple()
		ASSERT_IS_EQUAL(_.val, tuple())
		ASSERT_IS_EQUAL(_.changed, tuple())
		_.val.add(1)
		ASSERT_IS_EQUAL(_.val, {1})
		ASSERT_IS_EQUAL(_.changed, {1})
		return
