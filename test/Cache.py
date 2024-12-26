# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Cache import *

from hashlib import sha256
from datetime import datetime, timedelta

from typing import Optional, Any
from time import sleep


class MemoryContext(Context):
	def __init__(self):
		self.context = {}
		return

	def set(self, key: Any, value: Any, expires: int = 0):
		key = sha256(str(key).encode()).hexdigest()
		exp = datetime.now() + timedelta(seconds=expires) if expires else None
		self.context[key] = (
			exp.timestamp() if expires else 0,
			value,
		)
		return
	
	def get(self, key: Any) -> Optional[Any]:
		key = sha256(str(key).encode()).hexdigest()
		if key not in self.context.keys(): return None
		now = datetime.now().timestamp()
		exp, v = self.context[key]
		if not exp:
			return v
		if now < exp:
			return v
		del self.context[key]
		return None


class TestSampleConfiguration(Case):

	@classmethod
	def setUpClass(self):
		Helper.Set(
			'Memory',
			MemoryContext,
		)
		return

	@Order(0)	
	@Parameterized(
		{'k': 'a', 'v': True, 'expires': None},
		{'k': 'b', 'v': True, 'expires': 1},
		{'k': 'c', 'v': 1, 'expires': None},
		{'k': 'd', 'v': 2, 'expires': 1},
		{'k': 'e', 'v': 3.0, 'expires': None},
		{'k': 'f', 'v': 4.0, 'expires': 1},
		{'k': 'g', 'v': 'string', 'expires': None},
		{'k': 'h', 'v': 'String', 'expires': 1},
		{'k': 'i', 'v': (1,2), 'expires': None},
		{'k': 'j', 'v': (3,4), 'expires': 1},
		{'k': 'k', 'v': [5,6], 'expires': None},
		{'k': 'l', 'v': [7,8], 'expires': 1},
		{'k': 'm', 'v': {9,10}, 'expires': None},
		{'k': 'n', 'v': {11,12}, 'expires': 1},
		{'k': 'o', 'v': {'a': 1, 'b': 2.0}, 'expires': None},
		{'k': 'p', 'v': {'a': 3, 'b': 4.0}, 'expires': 1},
	)
	def testGetSetExpires(self, k, v, expires: int = None):
		context = Helper.Get('Memory')
		context.set(k, v, expires=expires)
		ASSERT_IS_EQUAL(context.get(k), v)
		if expires:
			sleep(expires + 1)
			ASSERT_IS_EQUAL(context.get(k), None)
		return
	
	@Order(1)
	def testFunctionCache(self):
		@Cached('Memory', expires=3)
		def foo(a, b):
			return a * b
		ASSERT_IS_EQUAL(foo(1,2), 2)
		ASSERT_IS_EQUAL(foo(1,2), 2)
		sleep(4)
		ASSERT_IS_EQUAL(foo(1,2), 2)
		return
	
	@Order(2)
	def testMethodCache(self):
		class Sample(object):
			@Cached('Memory', expires=3)
			def foo(self, a, b):
				return a + b
		_ = Sample()
		ASSERT_IS_EQUAL(_.foo(2, 3), 5)
		ASSERT_IS_EQUAL(_.foo(2, 3), 5)
		sleep(4)
		ASSERT_IS_EQUAL(_.foo(2, 3), 5)
		return
