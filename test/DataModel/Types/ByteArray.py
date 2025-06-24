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


class TestDataModelWithByteArray(Case):

	@Order(1)
	def testValue(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=bytearray,
				va=Validator(IsByteArray()),
			)
		_ = TestModel(val=bytearray([1, 2, 3]))
		ASSERT_IS_EQUAL(_.val, bytearray([1, 2, 3]))
		_.val = bytearray([])
		ASSERT_IS_EQUAL(_.val, bytearray([]))
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
				type=bytearray,
				va=Validator(IsByteArray()),
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_.val = bytearray([1, 2, 3])
		ASSERT_IS_EQUAL(_.val, bytearray([1, 2, 3]))
		_.val = bytearray([])
		ASSERT_IS_EQUAL(_.val, bytearray([]))
		_.val = None
		ASSERT_IS_EQUAL(_.val, None)
		class TestModel(
			Model,
		):
			val = Value(
				type=bytearray,
				va=Validator(IsByteArray()),
				default=bytearray([]),
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, bytearray([]))
		_.val = bytearray([1, 2, 3])
		ASSERT_IS_EQUAL(_.val, bytearray([1, 2, 3]))
		with ASSERT_EXCEPT(ValueError):
			_.val = None
		return

	@Order(3)
	def testValueWithDetectChangedElement(self):
		class TestHandler(
			Handler,
		):
			def __call__(self, o: 'TestModel', p: Value, v: bytearray, pv: bytearray):
				o.pval = pv
				return
		class TestModel(
			Model,
		):
			val = Value(
				type=bytearray,
				va=Validator(IsByteArray()),
				fn=TestHandler(),
				default=bytearray([]),
			)
			pval = Value(
				type=bytearray,
				va=Validator(IsByteArray()),
				default=None,
			)
		_ = TestModel()
		_.val.append(1)
		ASSERT_IS_EQUAL(_.val, bytearray([1]))
		ASSERT_IS_EQUAL(_.pval, bytearray([]))
		return