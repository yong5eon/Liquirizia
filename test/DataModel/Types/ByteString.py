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

from six import b


class TestDataModelWithByteString(Case):

	@Order(1)
	def testValue(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=bytes,
				va=Validator(IsByteString()),
			)
		_ = TestModel(val=b'123')
		ASSERT_IS_EQUAL(_.val, b'123')
		_.val = b''
		ASSERT_IS_EQUAL(_.val, b'')
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
				type=bytes,
				va=Validator(IsByteString()),
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_.val = b'123'
		ASSERT_IS_EQUAL(_.val, b'123')
		_.val = b''
		ASSERT_IS_EQUAL(_.val, b'')
		_.val = None
		ASSERT_IS_EQUAL(_.val, None)
		class TestModel(
			Model,
		):
			val = Value(
				type=bytes,
				va=Validator(IsByteString()),
				default=b'',
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, b'')
		_.val = b'123'
		ASSERT_IS_EQUAL(_.val, b'123')
		with ASSERT_EXCEPT(ValueError):
			_.val = None
		return

	@Order(3)
	def testValueWithDetectChangedElement(self):
		class TestHandler(
			Handler,
		):
			def __call__(self, o: 'TestModel', p: Value, v: bytes, pv: bytes):
				o.pval = pv
				return
		class TestModel(
			Model,
		):
			val = Value(
				type=bytes,
				va=Validator(IsByteString()),
				fn=TestHandler(),
				default=b'',
			)
			pval = Value(
				type=bytes,
				va=Validator(IsByteString()),
				default=None,
			)
		_ = TestModel()
		_.val += b'1'
		ASSERT_IS_EQUAL(_.val, b'1')
		ASSERT_IS_EQUAL(_.pval, b'')
		return