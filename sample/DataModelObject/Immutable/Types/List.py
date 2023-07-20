# -*- coding: utf-8 -*-

from Liquirizia.DataModelObject.Immutable.Types import *

from Liquirizia.Validator.Patterns import *

from sys import stderr


if __name__ == '__main__':

	try:
		a = List((4, 2, 8), IsRange(0, 10, 2))
		print(len(a))
		print(a)
		print(a[0])
		print(a[1])
		print(a[2])
		for v in a:
			print(v)
		for i, v in enumerate(a):
			print('{} : {}'.format(i, v))
		a[0] = 3  # expected RuntimeError exception
		for v in a:
			print(v)
		for i, v in enumerate(a):
			print('{} : {}'.format(i, v))
	except Exception as e:
		print(str(e), file=stderr)
