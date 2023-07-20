# -*- coding: utf-8 -*-

from Liquirizia.DataModelObject.Immutable.Types import *

from Liquirizia.Validator.Patterns import *

from sys import stderr


if __name__ == '__main__':

	try:
		# print(String(0))  # expect RuntimeError exception
		print(String('A'))
		print(String('B'))
		print(String('C', IsIn('A', 'B', 'C')))  # expect RuntimeError exception
		print(int(String('9')))
		print(float(String('9')))
		print(String('A') + 'B')
		print(String('A') + String('B'))
		print(String('A') * 1)
		print(String('A') * 5)
		print(String('A') == 'A')
		print(String('A') == String('A'))
		print(String('A') != 'B')
		print(String('A') != String('B'))
		print(not String('C'))
		print(not String(''))
	except Exception as e:
		print(str(e), file=stderr)

