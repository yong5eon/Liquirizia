# -*- coding: utf-8 -*-

from Liquirizia import (
	Virtual,
)

from sys import stderr


class BaseClass(object):
	def __init__(self, v):
		self.v = v
		return

	def __repr__(self):
		return str(self.v)

	@Virtual
	def a(self, v):
		pass

	@Virtual
	def b(self, v):
		pass


class DerivedClass(BaseClass):

	def a(self, v):
		self.v = v
		return


if __name__ == '__main__':
	base = BaseClass(1)

	try:
		base.a(2)  # expected raise NotImplementedError
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(base)

	try:
		base.b(2)	 # expected raise NotImplementedError
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(base)

	derived = DerivedClass(1)

	try:
		derived.a(3)
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(derived)

	try:
		derived.b(5)  # expected raise NotImplementedError
	except Exception as e:
		print(str(e), file=stderr)
	else:
		print(derived)
