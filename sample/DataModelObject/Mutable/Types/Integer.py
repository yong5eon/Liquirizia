# -*- coding: utf-8 -*-

from Liquirizia.DataModelObject.Mutable.Types import *

from Liquirizia.Validator.Patterns import *

from sys import stderr


if __name__ == '__main__':

	try:
		_ = Integer(9)
		print(type(_))
		print(isinstance(_, int))
		print('Expected None : {}'.format(Integer(None)))
		print('Expected 1 : {}'.format(Integer(1)))
		print('Expected 2 : {}'.format(Integer(2)))
		print('Expected 9 : {}'.format(Integer(9, IsGreaterEqualTo(1), IsLessEqualTo(9))))
		print('Expected 9 : {}'.format(int(Integer(9, IsGreaterEqualTo(1), IsLessEqualTo(9)))))
		print('Expected 9.0 : {}'.format(float(Integer(9, IsGreaterEqualTo(1), IsLessEqualTo(9)))))
		print('Expected 3 : {}'.format(Integer(2) + 1))
		print('Expected 3 : {}'.format(Integer(2) + Integer(1)))
		_ = Integer(2)
		_ += 1
		print('Expected 3 : {}'.format(_))
		_ += Integer(1)
		print('Expected 4 : {}'.format(_))
		print('Expected 4 : {}'.format(Integer(2) * 2))
		print('Expected 4 : {}'.format(Integer(2) * Integer(2)))
		print('Expected 1 : {}'.format(Integer(2) - 1))
		print('Expected 1 : {}'.format(Integer(2) - Integer(1)))
		print('Expected 1.5 : {}'.format(Integer(6) / 4))
		print('Expected 1.5 : {}'.format(Integer(6) / Integer(4)))
		print('Expected 1 : {}'.format(Integer(3) % 2))
		print('Expected 1 : {}'.format(Integer(3) % Integer(2)))
		print('Expected -2 : {}'.format(-Integer(2)))
		print('Expected 2 : {}'.format(-Integer(-2)))
		print('Expected 2 : {}'.format(+Integer(2)))
		print('Expected -2 : {}'.format(+Integer(-2)))
		print('Expected True : {}'.format(Integer(2) == 2))
		print('Expected True : {}'.format(Integer(2) == Integer(2)))
		print('Expected True : {}'.format(Integer(2) != 1))
		print('Expected True : {}'.format(Integer(2) != Integer(1)))
		print('Expected True : {}'.format(not Integer(0)))
		print('Expected False : {}'.format(not Integer(2)))
		print('Expected False : {}'.format(Integer(2) > 2))
		print('Expected False : {}'.format(Integer(2) > Integer(2)))
		print('Expected True : {}'.format(Integer(2) >= 2))
		print('Expected True : {}'.format(Integer(2) >= Integer(2)))
		print('Expected True : {}'.format(Integer(2) <= 2))
		print('Expected True : {}'.format(Integer(2) <= Integer(2)))
		print('Expected False : {}'.format(Integer(2) < 2))
		print('Expected False : {}'.format(Integer(2) < Integer(2)))
	except Exception as e:
		print(str(e), file=stderr)

	try:
		print(Integer(1.0))  # expect RuntimeError exception
	except Exception as e:
		print(str(e), file=stderr)

	try:
		print(Integer(0, IsGreaterEqualTo(1), IsLessEqualTo(9)))  # expect RuntimeError exception
	except Exception as e:
		print(str(e), file=stderr)

