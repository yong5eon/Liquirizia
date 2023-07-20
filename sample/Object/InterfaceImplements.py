# -*- coding: utf-8 -*-

from Liquirizia import (
	Interface,
	Implements,
)

from sys import stderr


@Interface
class Add(object):
	def add(self, other):
		pass


@Interface
class Minus(object):
	def sub(self, other):
		pass


@Interface
class Multiplication(object):
	def mul(self, other):
		pass


@Implements(Add, Minus, Multiplication)
class Calculator(object):
	def __init__(self, v):
		self.v = v
		return

	def add(self, other):
		return self.v + other

	def sub(self, other):
		return self.v - other


if __name__ == '__main__':

	cal = Calculator(10)

	try:
		print(cal.add(2))  # expected 12
		print(cal.sub(3))  # expected 7
		print(cal.mul(4))  # expected raise NotImplementedError
	except Exception as e:
		print(str(e), file=stderr)
