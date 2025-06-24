# -*- coding: utf-8 -*-

from Liquirizia.Test import *
from Liquirizia.DataModel import (
	Model,
	Value, 
	Handler,
)
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *

from datetime import time
from typing import Optional, Annotated


class TestDataModelWithTime(Case):

	@Order(1)
	def testValue(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=time,
				va=Validator(IsTime()),
			)
		_ = TestModel(val=time(0, 0, 0))
		ASSERT_IS_EQUAL(_.val, time(0, 0, 0))
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
				type=time,
				va=Validator(IsTime()),
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_.val = time(0, 0, 0)
		ASSERT_IS_EQUAL(_.val, time(0, 0, 0))
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
	
