# -*- coding: utf-8 -*-

from Liquirizia.DataModelObject.Mutable.Types import *

from Liquirizia.Validator.Patterns import *

from sys import stderr


if __name__ == '__main__':

	try:
		# print(Float(1.0))  # expect RuntimeError exception
		print(Float(1.0))
		print(Float(2.0))
		# print(Float(0.0, IsGreaterEqualTo(1.0), IsLessEqualTo(9)))  # expect RuntimeError exception
		print(Float(9.0, IsGreaterEqualTo(1.0), IsLessEqualTo(9)))
		print(int(Float(9.0, IsGreaterEqualTo(1.0), IsLessEqualTo(9))))
		print(float(Float(9.0, IsGreaterEqualTo(1.0), IsLessEqualTo(9))))
		print(Float(2.0) + 1)
		print(Float(2.0) + Float(1.0))
		print(Float(2.0) * 1)
		print(Float(2.0) * Float(1.0))
		print(Float(2.0) - 1)
		print(Float(2.0) - Float(1.0))
		print(Float(2.0) / 1)
		print(Float(2.0) / Float(1.0))
		print(Float(2.0) % 1)
		print(Float(2.0) % Float(1.0))
		print(-Float(2.0))
		print(+Float(2.0))
		print(Float(2.0) == 2)
		print(Float(2.0) == Float(2.0))
		print(Float(2.0) != 1)
		print(Float(2.0) != Float(1.0))
		print(not Float(0.0))
		print(not Float(2.0))
		print(Float(2.0) > 2)
		print(Float(2.0) > Float(2.0))
		print(Float(2.0) >= 2)
		print(Float(2.0) >= Float(2.0))
		print(Float(2.0) <= 2)
		print(Float(2.0) <= Float(2.0))
		print(Float(2.0) < 2)
		print(Float(2.0) < Float(2.0))
	except Exception as e:
		print(str(e), file=stderr)

