# -*- coding: utf-8 -*-

from Liquirizia.Test import *
from Liquirizia.DataModel import (
	Model,
	Value, 
	Handler,
)
from Liquirizia.Validator import Validator, Pattern
from Liquirizia.Validator.Patterns import *

from decimal import Decimal
from datetime import datetime, date, time

from random import randint, random

from typing import Optional


class TestDataModel(Case):

	@Parameterized(
			{'excp': None, 'kwargs': {'Val': 1, 'ValWithOutDescriptor': 2}},
			{'excp': ValueError, 'kwargs': {}},
			{'excp': ValueError, 'kwargs': {'Val': 1}},
			{'excp': ValueError, 'kwargs': {'ValWithOutDescriptor': 2}},
			{'excp': TypeError, 'kwargs': {'Val': 1.0, 'ValWithOutDescriptor': 2}},
			{'excp': TypeError, 'kwargs': {'Val': 1, 'ValWithOutDescriptor': 2.0}},
	)
	@Order(0)
	def testInit(self, excp, kwargs):
		class TestModel(Model):
			OptionVal: int = Value(va=Validator(IsToNone(IsTypeOf(int))))
			OptionValWithDefault: int = Value(va=Validator(IsToNone(IsTypeOf(int))), default=1)
			OptionValWithOutDescriptor: Optional[int]
			OptionValWithOutDescriptorWithDefault: Optional[int] = 0
			Val: int = Value(va=Validator(IsNotToNone(IsTypeOf(int))))
			ValWithDefault: int = Value(va=Validator(IsNotToNone(IsTypeOf(int))), default=9)
			ValWithOutDescriptor: int
			ValWithOutDescriptorWithNone: int = None
			ValWithOutDescriptorWithDefault: int = 0
		if excp:
			with ASSERT_EXCEPT(excp):
				_ = TestModel(**kwargs)
				_.OptionVal = randint(0, 65535)
				_.OptionValWithDefault = randint(0, 65535)
				_.OptionValWithOutDescriptor = randint(0, 65535)
				_.OptionValWithOutDescriptorWithDefault = randint(0, 65535)
				_.Val = randint(0, 65535)
				_.ValWithDefault = randint(0, 65535)
				_.ValWithOutDescriptor = randint(0, 65535)
				_.ValWithOutDescriptorWithNone = randint(0, 65535)
				_.ValWithOutDescriptorWithDefault = randint(0, 65535)
				_.OptionVal = None
				_.OptionValWithDefault = None
				_.OptionValWithOutDescriptor = None
				_.OptionValWithOutDescriptorWithDefault = None
				with ASSERT_EXCEPT(ValueError): _.Val = None
				with ASSERT_EXCEPT(ValueError): _.ValWithDefault = None
				with ASSERT_EXCEPT(ValueError): _.ValWithOutDescriptor = None
				with ASSERT_EXCEPT(ValueError): _.ValWithOutDescriptorWithDefault = None
				with ASSERT_EXCEPT(TypeError): _.OptionVal = random()
				with ASSERT_EXCEPT(TypeError): _.OptionValWithDefault = random()
				with ASSERT_EXCEPT(TypeError): _.OptionValWithOutDescriptor = random()
				with ASSERT_EXCEPT(TypeError): _.OptionValWithOutDescriptorWithDefault = random()
				with ASSERT_EXCEPT(TypeError): _.Val = random()
				with ASSERT_EXCEPT(TypeError): _.ValWithDefault = random()
				with ASSERT_EXCEPT(TypeError): _.ValWithOutDescriptor = random()
				with ASSERT_EXCEPT(TypeError): _.ValWithOutDescriptorWithNone = random()
				with ASSERT_EXCEPT(TypeError): _.ValWithOutDescriptorWithDefault = random()
		else:
			_ = TestModel(**kwargs)
			_.OptionVal = randint(0, 65535)
			_.OptionValWithDefault = randint(0, 65535)
			_.OptionValWithOutDescriptor = randint(0, 65535)
			_.OptionValWithOutDescriptorWithDefault = randint(0, 65535)
			_.Val = randint(0, 65535)
			_.ValWithDefault = randint(0, 65535)
			_.ValWithOutDescriptor = randint(0, 65535)
			_.ValWithOutDescriptorWithNone = randint(0, 65535)
			_.ValWithOutDescriptorWithDefault = randint(0, 65535)
			_.ValWithOutDescriptorWithNone = None
			_.OptionVal = None
			_.OptionValWithDefault = None
			_.OptionValWithOutDescriptor = None
			_.OptionValWithOutDescriptorWithDefault = None
			with ASSERT_EXCEPT(ValueError): _.Val = None
			with ASSERT_EXCEPT(ValueError): _.ValWithDefault = None
			with ASSERT_EXCEPT(ValueError): _.ValWithOutDescriptor = None
			with ASSERT_EXCEPT(ValueError): _.ValWithOutDescriptorWithDefault = None
			with ASSERT_EXCEPT(TypeError): _.OptionVal = random()
			with ASSERT_EXCEPT(TypeError): _.OptionValWithDefault = random()
			with ASSERT_EXCEPT(TypeError): _.OptionValWithOutDescriptor = random()
			with ASSERT_EXCEPT(TypeError): _.OptionValWithOutDescriptorWithDefault = random()
			with ASSERT_EXCEPT(TypeError): _.Val = random()
			with ASSERT_EXCEPT(TypeError): _.ValWithDefault = random()
			with ASSERT_EXCEPT(TypeError): _.ValWithOutDescriptor = random()
			with ASSERT_EXCEPT(TypeError): _.ValWithOutDescriptorWithNone = random()
			with ASSERT_EXCEPT(TypeError): _.ValWithOutDescriptorWithDefault = random()
		return

	@Parameterized(
			{'v': True},
			{'v': False},
	)
	@Order(1)
	def testBool(self, v):
		class TestModel(Model):
			v: Optional[bool]
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, bool)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, bool)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)
		return

	@Parameterized(
			{'v': 0},
			{'v': 1},
			{'v': 2},
			{'v': 3},
			{'v': 4},
			{'v': 5},
	)
	@Order(2)
	def testInteger(self, v):
		class TestModel(Model):
			v: Optional[int]
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, int)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, int)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)
		return

	@Parameterized(
			{'v': 0.},
			{'v': 1.},
			{'v': 2.},
			{'v': 3.},
			{'v': 4.},
			{'v': 5.},
	)
	@Order(3)
	def testFloat(self, v):
		class TestModel(Model):
			v: Optional[float]
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, float)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, float)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)
		return

	@Parameterized(
			{'v': 'Hello'},
			{'v': 'Hi'},
	)
	@Order(4)
	def testString(self, v):
		class TestModel(Model):
			v: Optional[str]
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, str)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, str)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)
		return

	@Parameterized(
			{'v': [True, False]},
			{'v': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
			{'v': [0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]},
			{'v': ['Hello', 'World', 'Nice', 'to', 'meet', 'you']},
			{'v': [True, 0, 0., 1, 1.0, 'Hello', 'Hi']},
			{'v': [(1,), (2,)]},
			{'v': [[1,], [2,]]},
			{'v': [{'a': 1, 'b': 2},{}]},
	)
	@Order(5)
	def testList(self, v):
		class TestModel(Model):
			v: Optional[list]
		_ = TestModel()
		ASSERT_IS_NONE(_.v)
		_.v = []
		ASSERT_IS_NOT_NONE(_.v)
		for n in v:
			_.v.append(n)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL_LIST(v, list(_.v))
		_.v = v
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL_LIST(v, list(_.v))
		return

	@Parameterized(
			{'v': (True, False)},
			{'v': (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)},
			{'v': (0., 1., 2., 3., 4., 5., 6., 7., 8., 9.)},
			{'v': ('Hello', 'World', 'Nice', 'to', 'meet', 'you')},
			{'v': (True, 0, 0., 1, 1.0, 'Hello', 'Hi')},
			{'v': ((1,), (2,))},
			{'v': ([1,], [2,])},
			{'v': ({'a': 1, 'b': 2},{})},
	)
	@Order(6)
	def testTuple(self, v):
		class TestModel(Model):
			v: Optional[tuple]
		_ = TestModel()
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL_TUPLE(v, tuple(_.v))
		return

	@Parameterized(
			{'v': {}},
			{'v': {'a': 1, 'b': 0.1, 'c': 'Hi', 'd': True, 'e': [1], 'f': (1,), 'g': {'a': 1, 'b': 0.3}}},
	)
	@Order(8)
	def testDict(self, v):
		class TestModel(Model):
			v: Optional[dict]
		_ = TestModel()
		ASSERT_IS_NONE(_.v)
		o = {}
		_.v = {}
		ASSERT_IS_NOT_NONE(_.v)
		for k, kv in v.items():
			o[k] = kv
			_.v[k] = kv
		ASSERT_IS_NOT_NONE(_.v)
		for k, kv in o.items():
			if isinstance(kv, list):
				ASSERT_IS_EQUAL_LIST(kv, list(_.v[k]))
				continue
			if isinstance(kv, tuple):
				ASSERT_IS_EQUAL_TUPLE(kv, tuple(_.v[k]))
				continue
			if isinstance(kv, dict):
				ASSERT_IS_EQUAL_DICT(kv, dict(_.v[k]))
			if isinstance(kv, Model): continue
			ASSERT_IS_EQUAL(kv, _.v[k])
		_.v = v
		ASSERT_IS_NOT_NONE(_.v)
		for k, kv in o.items():
			if isinstance(kv, list):
				ASSERT_IS_EQUAL_LIST(kv, list(_.v[k]))
				continue
			if isinstance(kv, tuple):
				ASSERT_IS_EQUAL_TUPLE(kv, tuple(_.v[k]))
				continue
			if isinstance(kv, dict):
				ASSERT_IS_EQUAL_DICT(kv, dict(_.v[k]))
			if isinstance(kv, Model): continue
			ASSERT_IS_EQUAL(kv, _.v[k])
		return

	@Parameterized(
			{'v': Decimal(0.)},
			{'v': Decimal(1.)},
			{'v': Decimal(2.)},
			{'v': Decimal(3.)},
			{'v': Decimal(4.)},
			{'v': Decimal(5.)},
	)
	@Order(10)
	def testDecimal(self, v):
		class TestModel(Model):
			v: Optional[Decimal]
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, Decimal)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, Decimal)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)

	@Parameterized(
			{'v': 1, 'const': 3},
			{'v': 2, 'const': 3},
			{'v': 3, 'const': 3},
			{'v': 4, 'const': 3},
			{'v': 5, 'const': 3},
	)
	@Order(90)
	def testHandler(self, v, const):
		class TestHandler(Handler):
			def __init__(self, v):
				self.v = v
				return
			def __call__(self, m, o, v, pv):
				m.b = m.a + self.v
				return
		class TestModel(Model):
			a = Value(Validator(IsToNone(IsInteger())), fn=TestHandler(const))
			b = Value(Validator(IsToNone(IsInteger())))
		_ = TestModel()
		ASSERT_IS_NONE(_.a)
		ASSERT_IS_NONE(_.b)
		_.a = v
		ASSERT_IS_EQUAL(v, _.a)
		ASSERT_IS_EQUAL(v + const, _.b)
		return
		