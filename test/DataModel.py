# -*- coding: utf-8 -*-

from Liquirizia.Test import *


from Liquirizia.DataModel import (
	Model,
	Attribute, 
	Handler,
)
from Liquirizia.Validator import Validator, Pattern
from Liquirizia.Validator.Patterns import *

from decimal import Decimal
from datetime import datetime, date, time


class TestDataModel(Case):

	@Parameterized(
			{'v': True},
			{'v': False},
	)
	@Order(1)
	def testBool(self, v):
		class TestModel(Model):
			v = Attribute(Validator(IsToNone(IsBool())))
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
			v = Attribute(Validator(IsToNone(IsInteger())))
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
			v = Attribute(Validator(IsToNone(IsFloat())))
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, float)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, float)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)
		return

	@Parameterized(
			{'v': Decimal(0.)},
			{'v': Decimal(1.)},
			{'v': Decimal(2.)},
			{'v': Decimal(3.)},
			{'v': Decimal(4.)},
			{'v': Decimal(5.)},
	)
	@Order(4)
	def testDecimal(self, v):
		class TestModel(Model):
			v = Attribute(Validator(IsToNone(IsDecimal())))
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, Decimal)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, Decimal)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)

	@Parameterized(
			{'v': 'Hello'},
			{'v': 'Hi'},
	)
	@Order(5)
	def testString(self, v):
		class TestModel(Model):
			v = Attribute(Validator(IsToNone(IsString())))
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, str)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, str)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)
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
			v = Attribute(Validator(IsToNone(IsTuple())))
		_ = TestModel()
		ASSERT_IS_NONE(_.v)
		l = []
		_.v = []
		ASSERT_IS_NOT_NONE(_.v)
		for n in v:
			l.append(n)	
			_.v.append(n)
		ASSERT_IS_NOT_NONE(_.v)
		for i, n in enumerate(l):
			if isinstance(n, (list, tuple)):
				ASSERT_IS_EQUAL(n, _.v[i])
				continue
			if isinstance(n, dict):
				ASSERT_IS_EQUAL(n, _.v[i])
				continue
			if isinstance(n, Model): 
				ASSERT_IS_EQUAL(n, _.v[i])
				continue
			ASSERT_IS_EQUAL(n, _.v[i])


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
	@Order(7)
	def testList(self, v):
		class TestModel(Model):
			v = Attribute(Validator(IsToNone(IsList())))
		_ = TestModel()
		ASSERT_IS_NONE(_.v)
		l = []
		_.v = []
		ASSERT_IS_NOT_NONE(_.v)
		for n in v:
			l.append(n)	
			_.v.append(n)
		ASSERT_IS_NOT_NONE(_.v)
		for i, n in enumerate(l):
			if isinstance(n, (list, tuple)):
				ASSERT_IS_EQUAL(n, _.v[i])
				continue
			if isinstance(n, dict):
				ASSERT_IS_EQUAL(n, _.v[i])
				continue
			if isinstance(n, Model): 
				ASSERT_IS_EQUAL(n, _.v[i])
				continue
			ASSERT_IS_EQUAL(n, _.v[i])
			return

	@Parameterized(
			{'v': {}},
			{'v': {'a': 1, 'b': 0.1, 'c': 'Hi', 'd': True, 'e': [1], 'f': (1,), 'g': {'a': 1, 'b': 0.3}}},
	)
	@Order(8)
	def testDict(self, v):
		class TestModel(Model):
			v = Attribute(Validator(IsToNone(IsDictionary())))
		_ = TestModel()
		ASSERT_IS_NONE(_.v)
		o = {}
		_.v = {}
		ASSERT_IS_NOT_NONE(_.v)
		for k, v in v.items():
			o[k] = v
			_.v[k] = v
		ASSERT_IS_NOT_NONE(_.v)
		for k, v in o.items():
			if isinstance(v, (list, tuple)):
				ASSERT_IS_EQUAL(v, _.v[k])
				continue
			if isinstance(v, dict):
				ASSERT_IS_EQUAL(v, _.v[k])
			if isinstance(v, Model): continue
			ASSERT_IS_EQUAL(v, _.v[k])
			return

	@Parameterized(
			{'v': 1, 'const': 3},
			{'v': 2, 'const': 3},
			{'v': 3, 'const': 3},
			{'v': 4, 'const': 3},
			{'v': 5, 'const': 3},
	)
	@Order(9)
	def testHandler(self, v, const):
		class TestHandler(Handler):
			def __init__(self, v):
				self.v = v
				return
			def __call__(self, model, obj, attr, value, previousValue):
				obj.b = obj.a + self.v
				return
		class TestModel(Model):
			a = Attribute(Validator(IsToNone(IsInteger())), fn=TestHandler(const))
			b = Attribute(Validator(IsToNone(IsInteger())))
		_ = TestModel()
		ASSERT_IS_NONE(_.a)
		ASSERT_IS_NONE(_.b)
		_.a = v
		ASSERT_IS_EQUAL(v, _.a)
		ASSERT_IS_EQUAL(v + const, _.b)
		return
		