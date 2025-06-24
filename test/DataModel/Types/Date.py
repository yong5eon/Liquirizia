# -*- coding: utf-8 -*-

from Liquirizia.Test import *
from Liquirizia.DataModel import (
	Model,
	Value, 
	Handler,
)
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *

from datetime import date
from typing import Optional, Annotated


class TestDataModelWithDate(Case):

	@Order(1)
	def testValue(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=date,
				va=Validator(IsDate()),
			)
		_ = TestModel(val=date(2025, 1, 1))
		ASSERT_IS_EQUAL(_.val, date(2025, 1, 1))
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
				type=date,
				va=Validator(IsDate()),
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_.val = date(2025, 1, 1)
		ASSERT_IS_EQUAL(_.val, date(2025, 1, 1))
		_.val = None
		ASSERT_IS_EQUAL(_.val, None)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val=1)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val=1.0)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val='1.0')
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val='None')
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val=True)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val=False)
		return
	
