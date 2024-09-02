# -*- coding: utf-8 -*-

from Liquirizia.Test import *


from Liquirizia.DataModel import (
	Model,
	Attribute, 
	Handler,
)
from Liquirizia.Validator import Validator, Pattern
from Liquirizia.Validator.Patterns import *

from copy import copy, deepcopy


class TestDataModel(Case):

	@Parameterized(
			{'v': True},
			{'v': False},
	)
	@Order(1)
	def testBool(self, v):
		class TestModel(Model):
			v = Attribute(Validator(IsAbleToNone(IsBool())))
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, bool)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, bool)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)

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
			v = Attribute(Validator(IsAbleToNone(IsInteger())))
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, int)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, int)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)

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
			v = Attribute(Validator(IsAbleToNone(IsFloat())))
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, float)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, float)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)

	@Parameterized(
			{'v': 'Hello'},
			{'v': 'Hi'},
	)
	@Order(4)
	def testString(self, v):
		class TestModel(Model):
			v = Attribute(Validator(IsAbleToNone(IsString())))
		_ = TestModel()
		ASSERT_IS_NOT_INSTANCE(_.v, str)
		ASSERT_IS_NONE(_.v)
		_.v = v
		ASSERT_IS_INSTANCE(_.v, str)
		ASSERT_IS_NOT_NONE(_.v)
		ASSERT_IS_EQUAL(_.v, v)

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
	@Order(4)
	def testList(self, v):
		class TestModel(Model):
			v = Attribute(Validator(IsAbleToNone(IsListable())))
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
				ASSERT_IS_EQUAL(n, copy(_.v[i]))
				continue
			if isinstance(n, dict):
				ASSERT_IS_EQUAL(n, copy(_.v[i]))
			if isinstance(n, Model): continue
			ASSERT_IS_EQUAL(n, _.v[i])

	@Parameterized(
			{'v': {}},
			{'v': {'a': 1, 'b': 0.1, 'c': 'Hi', 'd': True, 'e': [1], 'f': (1,), 'g': {'a': 1, 'b': 0.3}}},
	)
	@Order(4)
	def testDict(self, v):
		class TestModel(Model):
			v = Attribute(Validator(IsAbleToNone(IsDictionary())))
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
				ASSERT_IS_EQUAL(v, copy(_.v[k]))
				continue
			if isinstance(v, dict):
				ASSERT_IS_EQUAL(v, copy(_.v[k]))
			if isinstance(v, Model): continue
			ASSERT_IS_EQUAL(v, _.v[k])

	@Parameterized(
	)
	@Order(5)
	def testHandler(self, v, const):
		class TestHandler(Handler):
			def __init__(self, v):
				self.v = v
				return
			def __call__(self, model: any, attr: any, value: any, previousValue: any):
				model.b = model.a + self.v
				return
		class TestModel(Model):
			a = Attribute(Validator(IsAbleToNone(IsInteger())), fn=TestHandler(const))
			b = Attribute(Validator(IsAbleToNone(IsInteger())))
			_ = TestModel()
			ASSERT_IS_NONE(_.a)
			ASSERT_IS_NONE(_.b)
			_.a = v
			ASSERT_IS_EQUAL(v, _.a)
			ASSERT_IS_EQUAL(v + const, _.b)
		

