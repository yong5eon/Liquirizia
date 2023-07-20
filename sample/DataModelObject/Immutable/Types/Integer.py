# -*- coding: utf-8 -*-

from Liquirizia.DataModelObject.Immutable.Types import *

from Liquirizia.Validator.Patterns import *

from sys import stderr


if __name__ == '__main__':

	try:
		# print(Integer(1.0))  # expect RuntimeError exception
		print(Integer(None))
		print(Integer(1))
		print(Integer(2))
		# print(Integer(0, IsGreaterEqualTo(1), IsLessEqualTo(9)))  # expect RuntimeError exception
		print(Integer(9, IsGreaterEqualTo(1), IsLessEqualTo(9)))
		print(int(Integer(9, IsGreaterEqualTo(1), IsLessEqualTo(9))))
		print(float(Integer(9, IsGreaterEqualTo(1), IsLessEqualTo(9))))
		print(Integer(2) + 1)
		print(Integer(2) + Integer(1))
		print(Integer(2) * 1)
		print(Integer(2) * Integer(1))
		print(Integer(2) - 1)
		print(Integer(2) - Integer(1))
		print(Integer(2) / 1)
		print(Integer(2) / Integer(1))
		print(Integer(2) % 1)
		print(Integer(2) % Integer(1))
		print(-Integer(2))
		print(+Integer(2))
		print(Integer(2) == 2)
		print(Integer(2) == Integer(2))
		print(Integer(2) != 1)
		print(Integer(2) != Integer(1))
		print(not Integer(0))
		print(not Integer(2))
		print(Integer(2) > 2)
		print(Integer(2) > Integer(2))
		print(Integer(2) >= 2)
		print(Integer(2) >= Integer(2))
		print(Integer(2) <= 2)
		print(Integer(2) <= Integer(2))
		print(Integer(2) < 2)
		print(Integer(2) < Integer(2))
	except Exception as e:
		print(str(e), file=stderr)

