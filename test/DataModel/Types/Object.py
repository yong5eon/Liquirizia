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


class TestDataModelWithObject(Case):

	@Order(1)
	def testValue(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=dict,
				va=Validator(IsObject()),
			)
		_ = TestModel(val={'a': 1, 'b': 2.0, 'c': '3'})
		ASSERT_IS_EQUAL(_.val, {'a': 1, 'b': 2.0, 'c': '3'})
		_.val['d'] = True
		ASSERT_IS_EQUAL(_.val, {'a': 1, 'b': 2.0, 'c': '3', 'd': True})
		_.val = {}
		ASSERT_IS_EQUAL(_.val, {})
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
				type=dict,
				va=Validator(IsObject()),
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_.val = {'a': 1, 'b': 2.0, 'c': '3'}
		ASSERT_IS_EQUAL(_.val, {'a': 1, 'b': 2.0, 'c': '3'})
		_.val['d'] = True
		ASSERT_IS_EQUAL(_.val, {'a': 1, 'b': 2.0, 'c': '3', 'd': True})
		_.val = {}
		ASSERT_IS_EQUAL(_.val, {})
		_.val = None
		ASSERT_IS_EQUAL(_.val, None)
		class TestModel(
			Model,
		):
			val = Value(
				type=dict,
				va=Validator(IsObject()),
				default={},
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, {})
		_.val = {'a': 1, 'b': 2.0, 'c': '3'}
		ASSERT_IS_EQUAL(_.val, {'a': 1, 'b': 2.0, 'c': '3'})
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
				type=dict,
				va=Validator(IsObject()),
				fn=TestHandler(),
				default={},
			)
			pval = Value(
				type=dict,
				va=Validator(IsObject()),
				default=None,
			)
		_ = TestModel()
		_.val['a'] = 1
		ASSERT_IS_EQUAL(_.val, {'a': 1})
		ASSERT_IS_EQUAL(_.pval, {})
		_.val['b'] = 2.0
		ASSERT_IS_EQUAL(_.val, {'a': 1, 'b': 2.0})
		ASSERT_IS_EQUAL(_.pval, {'a': 1})
		_.val['c'] = '3'
		ASSERT_IS_EQUAL(_.val, {'a': 1, 'b': 2.0, 'c': '3'})
		ASSERT_IS_EQUAL(_.pval, {'a': 1, 'b': 2.0})
		_.val = {}
		ASSERT_IS_EQUAL(_.val, {})
		ASSERT_IS_EQUAL(_.pval, {'a': 1, 'b': 2.0, 'c': '3'})
		return