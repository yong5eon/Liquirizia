# -*- coding: utf-8 -*-

from Liquirizia.Validator import Validator, Pattern, Error

from Liquirizia.Test import (
	Case,
	ASSERT,
)
from Liquirizia.Test.Patterns import (
	IsEqualTo as AssertEqualTo,
	IsNotEqualTo as AssertNotEqualTo,
	IsTrue as AssertTrue,
	IsFalse as AssertFalse,
	IsExceptionWith as AssertExceptionWith,
)
from operator import eq


class IsNotNone(Pattern):
	def __call__(self, parameter):
		if parameter is None:
			raise ValueError('Value Error : {} must be not None'.format(parameter))
		return parameter

class IsOK(Pattern):
	def __init__(self, *args):
		self.args = []
		for v in args:
			if isinstance(v, str):
				self.args.append(v.upper())
			else:
				self.args.append(v)
		return
	def __call__(self, parameter):
		if isinstance(parameter, str):
			p = parameter.upper()
		else:
			p = parameter
		if p in self.args:
			return True
		raise ValueError('Value Error : {} must be in {}'.format(parameter, self.args))


class IsTrue(Pattern):
	def __call__(self, parameter):
		if eq(parameter, True):
			return 1
		raise ValueError('Value Error : {} must be True'.format(parameter))


class V(Case):
	def __init__(self, o, vps=()):
		self.va = Validator(*vps if isinstance(vps, (list, tuple)) else (vps,))
		self.o = o
		return
	def __call__(self):
		o = self.va(self.o)
		return o
	def __str__(self):
		return 'Validate({})'.format(self.o)


ASSERT(V(None, vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertExceptionWith(ValueError))
ASSERT(V(True, vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertEqualTo(True))
ASSERT(V(False, vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertExceptionWith(ValueError))
ASSERT(V(1, vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertEqualTo(True))
ASSERT(V(0, vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertExceptionWith(ValueError))
ASSERT(V('Y', vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertEqualTo(True))
ASSERT(V('N', vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertExceptionWith(ValueError))
ASSERT(V('y', vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertEqualTo(True))
ASSERT(V('n', vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertExceptionWith(ValueError))
ASSERT(V('YES', vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertEqualTo(True))
ASSERT(V('NO', vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertExceptionWith(ValueError))
ASSERT(V('yes', vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertEqualTo(True))
ASSERT(V('no', vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertExceptionWith(ValueError))
ASSERT(V('OK', vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertEqualTo(True))
ASSERT(V('ok', vps=(IsNotNone(), IsOK(True, 1, 'Y', 'YES', 'OK'))), AssertEqualTo(True))
