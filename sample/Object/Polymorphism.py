# -*- coding: utf-8 -*-

from Liquirizia import (
	Extends,
)

from sys import stderr


class CustomClass(object):

	@Extends
	def a(self, a):
		return a * a

	@Extends
	def a(self, a, b):
		return a * b


if __name__ == '__main__':

	obj = CustomClass()

	try:
		print(obj.a(2))  # expected 4
		print(obj.a(2, 3))  # expected 6
	except Exception as e:
		print(str(e), file=stderr)
