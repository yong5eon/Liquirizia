# -*- coding: utf-8 -*-

from Liquirizia.Validator import Validate, Validator, Pattern
from Liquirizia.Validator.Patterns import *

from sys import stderr

if __name__ == '__main__':

	# Validate True
	validator = Validator(IsNotNull(), IsNumeric(), IsEqualTo(1))
	parameter = 1
	try:
		parameter = validator(parameter)  # expect true
	except RuntimeError as e:
		print(str(e), file=stderr)
	else:
		print('{} is not empty, numeric and equaled to 1'.format(parameter))

	# Validate False
	validator = Validator(IsNotNull(), IsNumeric(), IsEqualTo(0))
	parameter = 1
	try:
		parameter = validator(parameter)  # expect false with raise exception
	except RuntimeError as e:
		print(str(e), file=stderr)
	else:
		print('{} is not empty, numeric and equaled to 0'.format(parameter))

	# Validate Your Pattern
	class IsOver(Pattern):

		def __init__(self, base):
			self.base = base
			return

		def __call__(self, parameter):
			if not parameter > self.base:
				raise RuntimeError('{} is not over {}'.format(parameter, self.base))
			return parameter

	validator = Validator(IsNotNull(), IsNumeric(), IsOver(0))
	parameter = 1
	try:
		parameter = validator(parameter)  # expect false with raise runtime error
	except RuntimeError as e:
		print(str(e), file=stderr)
	else:
		print('{} is not empty, number and over 0'.format(parameter))

	validator = Validator(IsNotNull(), IsNumeric(), IsOver(1))
	parameter = 1
	try:
		parameter = validator(parameter)  # expect true
	except RuntimeError as e:
		print(str(e), file=stderr)
	else:
		print('{} is not empty, number and over 1'.format(parameter))

	# Validate Integer
	validator = Validator(
		IsNotNull(),
		IsInteger(IsOver(0))
	)

	try:
		print('parameter is {}'.format(validator(1)))  # expect print 1
		print('parameter is {}'.format(validator(0)))  # expect raise RuntimeError
	except RuntimeError as e:
		print(str(e), file=stderr)

	# Validate Float
	validator = Validator(
		IsNotNull(),
		IsFloat(IsOver(0))
	)

	try:
		print('parameter is {}'.format(validator(1.0)))  # expect print 1.0
		print('parameter is {}'.format(validator(3)))  # expect raise RuntimeError
	except RuntimeError as e:
		print(str(e), file=stderr)

	# Validate String
	validator = Validator(
		IsNotNull(),
		IsNotEmptyString(),
		IsString(IsIn('허용선', '최준호', '홍승걸', '김진영', '방태식'))
	)

	try:
		print('parameter is {}'.format(validator('허용선')))  # expect print '허용선'
		print('parameter is {}'.format(validator('이기현')))  # expect raise RuntimeError
	except RuntimeError as e:
		print(str(e), file=stderr)

	# Validate List or Tuple
	validator = Validator(
		IsNotNull(),
		IsNotEmptyListable(),
		IsListable(IsOver(0))
	)

	parameter = []
	try:
		parameter = validator(parameter)  # expect false
	except RuntimeError as e:
		print(str(e), file=stderr)
	else:
		print('{} is listable, not empty and all elements are over 0'.format(parameter))

	parameter = [0, 1, 2, 3]
	try:
		parameter = validator(parameter)  # expect false
	except RuntimeError as e:
		print(str(e), file=stderr)
	else:
		print('{} is listable, not empty and all elements are over 0'.format(parameter))

	parameter = [1, 2, 3]
	try:
		parameter = validator(parameter)  # expect true
	except RuntimeError as e:
		print(str(e), file=stderr)
	else:
		print('{} is listable, not empty and all elements are over 0'.format(parameter))

	# Validate Dictionary
	parameter = {
		'a': 1,
		'b': 2,
		'c': 3,
		'd': None,
		'e': [4, 5, 6],
		'f': {
			'a': 10,
			'b': 11,
			'c': 12
		},
	}
	validator = Validator(
		IsNotNull(),
		IsNotEmptyDictionary(),
		IsRequiredInDictionary(('a', 'b', 'c', 'd')),
		IsDictionary({
			'a': Validator(IsNotNull(), IsNumeric(),),
			'b': Validator(IsNotNull(), IsNumeric(), IsEqualTo(2)),
			'c': Validator(IsNotNull(), IsNumeric(), IsIn(3, 4, 5, 6, 7, 8)),
			'd': Validator(SetDefault(4)),
			'e': Validator(IsListable(IsOver(3)), IsNotNull()),
			'f': Validator(
				IsNotEmptyDictionary(),
				IsRequiredInDictionary('a', 'b'),
				IsDictionary({
					'a': (IsNotNull(), IsNumeric()),
					'b': (IsNotNull(), IsNumeric(), IsOver(9)),
				})
			),
		})
	)
	try:
		parameter = validator(parameter)
	except RuntimeError as e:
		print(str(e), file=stderr)
	else:
		print('{} is objectable, not empty and all validates of elements are ok'.format(parameter))

	# Test Decorator with Function
	@Validate({
		'a': IsNotNull(),
		'b': (IsNotNull(), IsNumeric(), IsGreaterEqualTo(0)),
		'c': IsNotNull(),
		'd': (IsNotNull(), IsNumeric(), IsLessEqualTo(10)),
		'e': (IsNotEmptyListable(), IsListable(IsLessThan(5))),
		'f': (
			IsNotEmptyDictionary(),
			IsRequiredInDictionary('a', 'b'),
			IsDictionary({
				'a': (IsNotNull(), IsNumeric(), IsGreaterThan(0), IsLessThan(5)),
			})
		),
		'const': SetDefault(3),
	})
	def foo(a, b, c, d, e, f, const=None):
		return round((a + b + c + d) * sum(e) / sum(f.values()) % const)

	try:
		ret = foo(1, 2, 3, d=4, e=(1, 2, 3), f={'a': 2, 'b': 1})
	except RuntimeError as e:
		print(str(e), file=stderr)
	else:
		print('foo returned {}'.format(ret))

	# Test Decorator with Method of Class
	class A:
		@Validate({
			'a': IsNotNull(),
			'b': (IsNotNull(), IsNumeric(), IsGreaterEqualTo(0)),
			'c': IsNotNull(),
			'd': (IsNotNull(), IsNumeric(), IsLessEqualTo(10)),
			'e': (IsNotEmptyListable(), IsListable(IsLessThan(5))),
			'f': (
				IsNotEmptyDictionary(),
				IsRequiredInDictionary('a'),
				IsDictionary({
					'a': (IsNotNull(), IsNumeric(), IsGreaterThan(0), IsLessThan(5)),
				})
			),
			'const': SetDefault(3),
		})
		def foo(self, a, b, c, d, e, f, const=None):
			return round((a + b + c + d) * sum(e) / sum(f.values()) % const)

	try:
		a = A()
		ret = a.foo(1, 2, 3, d=4, e=(1, 2, 3), f={'a': 2, 'b': 1})
	except RuntimeError as e:
		print(str(e), file=stderr)
	else:
		print('A.foo returned {}'.format(ret))
