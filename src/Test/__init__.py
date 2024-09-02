# -*- coding: utf-8 -*-

from .Loader import Loader
from .Runner import Runner
from .Result import Result
from .Parameterized import Parameterized
from .Order import Order

from inspect import getouterframes, currentframe
from unittest import TestCase

__all__ = (
	'Case',
	'Result',
	'Runner',
	'Parameterized',
	'Order',
	'ASSERT_TRUE',
	'ASSERT_FALSE',
	'ASSERT_IS',
	'ASSERT_IS_NOT',
	'ASSERT_IS_NONE',
	'ASSERT_IS_NOT_NONE',
	'ASSERT_IS_IN',
	'ASSERT_IS_NOT_IN',
	'ASSERT_IS_INSTANCE',
	'ASSERT_IS_NOT_INSTANCE',
	'ASSERT_IS_EQUAL',
	'ASSERT_IS_NOT_EQUAL',
	'ASSERT_IS_EQUAL_ROUND',
	'ASSERT_IS_NOT_EQUAL_ROUND',
	'ASSERT_IS_GREATER',
	'ASSERT_IS_GREATER_EQUAL',
	'ASSERT_IS_LESS',
	'ASSERT_IS_LESS_EQUAL',
	'ASSERT_IS_REGEX',
	'ASSERT_IS_NOT_REGEX',
	'ASSERT_IS_EQUAL_COUNT',
	'ASSERT_IS_EQUAL_SEQUENCE',
	'ASSERT_IS_EQUAL_MULTILINE',
	'ASSERT_IS_EQUAL_LIST',
	'ASSERT_IS_EQUAL_TUPLE',
	'ASSERT_IS_EQUAL_SET',
	'ASSERT_IS_EQUAL_DICT',
	'ASSERT_EXCEPT',
	'ASSERT_EXCEPT_REGEX',
	'ASSERT_EXCEPT_REGEXP',
	'ASSERT_WARN',
	'ASSERT_WARN_REGEX',
	'ASSERT_WITH_LOG',
	'ASSERT_WITHOUT_LOG',
)


Case = TestCase

def ASSERT_TRUE(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertTrue(*args, **kwargs)

def ASSERT_FALSE(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertFalse(*args, **kwargs)

def ASSERT_IS(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertIs(*args, **kwargs)

def ASSERT_IS_NOT(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertIsNot(*args, **kwargs)

def ASSERT_IS_NONE(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertIsNone(*args, **kwargs)

def ASSERT_IS_NOT_NONE(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertIsNotNone(*args, **kwargs)

def ASSERT_IS_IN(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertIn(*args, **kwargs)

def ASSERT_IS_NOT_IN(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertNotIn(*args, **kwargs)

def ASSERT_IS_INSTANCE(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertIsInstance(*args, **kwargs)

def ASSERT_IS_NOT_INSTANCE(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertNotIsInstance(*args, **kwargs)

def ASSERT_IS_EQUAL(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertEqual(*args, **kwargs)

def ASSERT_IS_NOT_EQUAL(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertNotEqual(*args, **kwargs)

def ASSERT_IS_EQUAL_ROUND(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertAlmostEqual(*args, **kwargs)

def ASSERT_IS_NOT_EQUAL_ROUND(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertAlmostEqual(*args, **kwargs)

def ASSERT_IS_GREATER(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertGreater(*args, **kwargs)

def ASSERT_IS_GREATER_EQUAL(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertGreaterEqual(*args, **kwargs)

def ASSERT_IS_LESS(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertLess(*args, **kwargs)

def ASSERT_IS_LESS_EQUAL(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertLessEqual(*args, **kwargs)

def ASSERT_IS_REGEX(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertRegex(*args, **kwargs)

def ASSERT_IS_NOT_REGEX(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertNotRegex(*args, **kwargs)

def ASSERT_IS_EQUAL_COUNT(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertCountEqual(*args, **kwargs)

def ASSERT_IS_EQUAL_SEQUENCE(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertSequenceEqual(*args, **kwargs)

def ASSERT_IS_EQUAL_MULTILINE(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertMultiLineEqual(*args, **kwargs)

def ASSERT_IS_EQUAL_LIST(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertListEqual(*args, **kwargs)

def ASSERT_IS_EQUAL_TUPLE(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertTupleEqual(*args, **kwargs)

def ASSERT_IS_EQUAL_SET(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertSetEqual(*args, **kwargs)

def ASSERT_IS_EQUAL_DICT(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertDictEqual(*args, **kwargs)

def ASSERT_EXCEPT(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertRaises(*args, **kwargs)

def ASSERT_EXCEPT_REGEX(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertRaisesRegex(*args, **kwargs)

def ASSERT_EXCEPT_REGEXP(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertRaisesRegex(*args, **kwargs)

def ASSERT_WARN(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertWarns(*args, **kwargs)

def ASSERT_WARN_REGEX(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertWarnsRegex(*args, **kwargs)

def ASSERT_WITH_LOG(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertLogs(*args, **kwargs)

def ASSERT_WITHOUT_LOG(*args, **kwargs):
	parent = getouterframes(currentframe())[1]
	self = parent.frame.f_locals['self']
	if not isinstance(self, TestCase): return
	return self.assertNoLogs(*args, **kwargs)
