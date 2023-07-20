# -*- coding: utf-8 -*-

from Liquirizia import (
	Private,
	Protected,
)

from sys import stderr


class BaseClass(object):
	def __init__(self, v):
		self.v = v
		return

	def __repr__(self):
		return str(self.v)

	@Private
	def a(self, v):
		self.v = v
		return

	@Protected
	def b(self, v):
		self.v = v
		return

	def c(self, v):
		self.v = v
		return

	def d(self, v):
		self.a(v)
		return


class DerivedClass(BaseClass):

	def aa(self, v):
		super(DerivedClass, self).a(v)
		return

	def bb(self, v):
		super(DerivedClass, self).b(v)
		return

	def cc(self, v):
		super(DerivedClass, self).c(v)
		return

	def dd(self, v):
		super(DerivedClass, self).a(v)
		return


if __name__ == '__main__':
	base = BaseClass(1)

	try:
		base.a(2)  # expected raise RuntimeError
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(base)

	try:
		base.b(2)	 # expected raise RuntimeError
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(base)

	try:
		base.c(3)	 # expected 3
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(base)

	try:
		base.d(4)  # expected 4
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(base)

	derived = DerivedClass(1)

	try:
		derived.aa(5)  # expected raise RuntimeError
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(derived)

	try:
		derived.bb(6)  # expected 6
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(derived)

	try:
		derived.cc(7)  # expected 7
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(derived)

	try:
		derived.dd(8)  # expected raise RuntimeError
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(derived)
