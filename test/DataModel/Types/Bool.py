# -*- coding: utf-8 -*-

from Liquirizia.Test import *
from Liquirizia.DataModel import (
	Model,
	Value, 
	Handler,
)
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *

from typing import Optional, Annotated


class TestDataModelWithBool(Case):

	@Order(1)
	def testValue(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=bool,
				va=Validator(IsBool()),
			)
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
				type=bool,
				va=Validator(IsBool()),
				default=None
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_.val = True
		ASSERT_IS_EQUAL(_.val, True)
		_.val = False
		ASSERT_IS_EQUAL(_.val, False)
		_.val = None
		ASSERT_IS_EQUAL(_.val, None)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val=1)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val=0)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val='True')
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val='False')
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val='None')
		return
