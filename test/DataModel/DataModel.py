# -*- coding: utf-8 -*-

from Liquirizia.Test import *
from Liquirizia.DataModel import (
	Model,
	Value, 
	Handler,
)
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *

from decimal import Decimal
from datetime import datetime, date, time
from typing import Optional, Annotated


class TestDataModel(Case):

	@Order(1)
	def testValue(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=int
			)
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		with ASSERT_EXCEPT(ValueError):
			_ = TestModel()
		return
	
	@Order(2)
	def testValueWithDefault(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=int,
				default=1
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 1)
		return
	
	@Order(3)
	def testValueWithValidator(self):
		class TestModel(
			Model,
		):
			val = Value(
				type=int,
				va=Validator(IsInteger())
			)
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val=1.0)
		return
	
	@Order(4)
	def testValueWithModelHandler(self):
		class TestHandler(Handler):
			def __call__(self, o: 'TestModel', p: Value, v, pv):
				if p.name == 'val': o.pv = pv
				return
		
		class TestModel(
			Model,
		):
			val = Value(
				type=int,
				default=1,
				fn=TestHandler(),
			)
			pv = Value(
				type=int,
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 1)
		ASSERT_IS_EQUAL(_.pv, None)
		_.val = 2
		ASSERT_IS_EQUAL(_.val, 2)
		ASSERT_IS_EQUAL(_.pv, 1)
		return
	
	@Order(5)
	def testValueWithValueHandler(self):
		class TestHandler(Handler):
			def __call__(self, o: 'TestModel', p: Value, v, pv):
				o.pv = pv
				return
		
		class TestModel(
			Model,
		):
			val = Value(
				type=int,
				default=1,
				fn=TestHandler(),
			)
			pv = Value(
				type=int,
				default=None,
			)
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 1)
		ASSERT_IS_EQUAL(_.pv, None)
		_.val = 2
		ASSERT_IS_EQUAL(_.val, 2)
		ASSERT_IS_EQUAL(_.pv, 1)
		return
	
	@Order(6)
	def testType(self):
		class TestModel(
			Model,
		):
			val: int
		with ASSERT_EXCEPT(ValueError):
			_ = TestModel()
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		return
	
	@Order(7)
	def testTypeWithDefault(self):
		class TestModel(
			Model,
		):
			val: int = 1
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 1)
		_ = TestModel(val=2)
		ASSERT_IS_EQUAL(_.val, 2)
		return
	
	@Order(8)
	def testOptionalType(self):
		class TestModel(
			Model,
		):
			val: Optional[int]
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		_ = TestModel(val=None)
		ASSERT_IS_EQUAL(_.val, None)
		return
	
	@Order(9)
	def testOptionalTypeWithDefault(self):
		class TestModel(
			Model,
		):
			val: Optional[int] = 1
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 1)
		_ = TestModel(val=2)
		ASSERT_IS_EQUAL(_.val, 2)
		_ = TestModel(val=None)
		ASSERT_IS_EQUAL(_.val, None)
		return

	@Order(10)
	def testDescriptionAnnotatedType(self):
		class TestModel(
			Model,
		):
			val: Annotated[int, 'val, integer']
		with ASSERT_EXCEPT(ValueError):
			_ = TestModel()
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		return
	
	@Order(11)
	def testDescriptionAnnotatedTypeWithDefault(self):
		class TestModel(
			Model,
		):
			val: Annotated[int, 'val, integer'] = 0
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 0)
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		return

	@Order(12)
	def testDescriptionAnnotatedOptionalType(self):
		class TestModel(
			Model,
		):
			val: Annotated[Optional[int], 'val, integer']
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		return

	@Order(13)
	def testDescriptionAnnotatedOptionalTypeWithDefault(self):
		class TestModel(
			Model,
		):
			val: Annotated[Optional[int], 'val, integer'] = 0
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 0)
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		return
	
	@Order(14)
	def testParameterizedAnnotatedType(self):
		class TestModel(
			Model,
		):
			val: Annotated[int, {
				'description': 'val, integer',
			}]
		with ASSERT_EXCEPT(ValueError):
			_ = TestModel()
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		return
	
	@Order(15)
	def testParameterizedAnnotatedTypeWithDefault(self):
		class TestModel(
			Model,
		):
			val: Annotated[int, {
				'description': 'val, integer',
			}] = 0
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 0)
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		return
	
	@Order(16)
	def testParameterizedAnnotatedTypeWithValidator(self):
		class TestModel(
			Model,
		):
			val: Annotated[int, {
				'description': 'val, integer',
				'va': Validator(IsInteger()),
			}]
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		with ASSERT_EXCEPT(TypeError):
			_ = TestModel(val=1.0)
		return
	
	@Order(17)
	def testParameterizedAnnotatedTypeWithModelHandler(self):
		class TestHandler(Handler):
			def __call__(self, o: 'TestModel', p: Value, v, pv):
				if p.name == 'val': o.pv = pv
				return
		
		class TestModel(
			Model,
			fn=TestHandler(),
		):
			val: Annotated[int, {
				'description': 'val, integer',
			}] = 1
			pv: Annotated[int, {
				'description': 'previous value',
			}] = 2
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 1)
		ASSERT_IS_EQUAL(_.pv, 2)
		_.val = 2
		ASSERT_IS_EQUAL(_.val, 2)
		ASSERT_IS_EQUAL(_.pv, 1)
		_.val = 3
		ASSERT_IS_EQUAL(_.val, 3)
		ASSERT_IS_EQUAL(_.pv, 2)
		return

	@Order(18)
	def testParameterizedAnnotatedTypeWithValueHandler(self):
		class TestHandler(Handler):
			def __call__(self, o: 'TestModel', p: Value, v, pv):
				o.pv = pv
				return
		
		class TestModel(
			Model,
		):
			val: Annotated[int, {
				'fn': TestHandler(),
				'description': 'val, integer',
			}] = 1
			pv: Annotated[int, {
				'description': 'previous value',
			}] = None
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 1)
		ASSERT_IS_EQUAL(_.pv, None)
		_.val = 2
		ASSERT_IS_EQUAL(_.val, 2)
		ASSERT_IS_EQUAL(_.pv, 1)
		return

	@Order(19)
	def testParameterizedAnnotatedOptionalType(self):
		class TestModel(
			Model,
		):
			val: Annotated[Optional[int], {
				'description': 'val, integer',
			}]
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, None)
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		return

	@Order(20)
	def testParameterizedAnnotatedOptionalTypeWithDefault(self):
		class TestModel(
			Model,
		):
			val: Annotated[Optional[int], {
				'description': 'val, integer',
			}] = 0
		_ = TestModel()
		ASSERT_IS_EQUAL(_.val, 0)
		_ = TestModel(val=1)
		ASSERT_IS_EQUAL(_.val, 1)
		return
	
	@Order(21)
	def testNotSupportedType(self):
		PATTERNS = [
			bool,
			int,
			float,
			str,
			list,
			tuple,
			set,
			dict,
			bytes,
			bytearray,
			Decimal,
			datetime,
			date,
			time,
		]
		for t in PATTERNS:
			class TestModel(Model):
				val = Value(type=t)
		with ASSERT_EXCEPT(TypeError):
			class TestModel(Model):
				val: object
		with ASSERT_EXCEPT(TypeError):
			class TestModel(Model):
				val = Value(type=object)
		class TestObject(object): pass
		with ASSERT_EXCEPT(TypeError):
			class TestModel(Model):
				val = Value(type=TestObject)
		return
	