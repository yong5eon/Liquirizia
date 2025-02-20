# -*- coding: utf-8 -*-

from Liquirizia.Validator import Validate, Validator, Pattern
from Liquirizia.Validator.Patterns import *
from Liquirizia.Validator.Patterns.Array import *
from Liquirizia.Validator.Patterns.Dictionary import (
	IsRequiredIn as IsRequiredInDictionary,
	IsMappingOf as IsMappingOfDictionary,
)
from Liquirizia.Validator.Patterns.DataObject import (
	IsRequiredIn as IsRequiredInDataObject,
	IsMappingOf as IsMappingOfDataObject,
)

from dataclasses import dataclass
from sys import stderr

if __name__ == '__main__':

	# Validate True
	validator = Validator(IsNotToNone(), IsEqualTo(1))
	parameter = 1
	try:
		parameter = validator(parameter)  # expect true
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)
	else:
		print('{} is not empty, numeric and equaled to 1'.format(parameter))

	# Validate False
	validator = Validator(IsNotToNone(), IsEqualTo(0))
	parameter = 1
	try:
		parameter = validator(parameter)  # expect false with raise exception
	except (TypeError, ValueError) as e:
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
				raise ValueError('{} is not over {}'.format(parameter, self.base))
			return parameter

	validator = Validator(IsNotToNone(), IsOver(0))
	parameter = 1
	try:
		parameter = validator(parameter)  # expect false with raise runtime error
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)
	else:
		print('{} is not empty, number and over 0'.format(parameter))

	validator = Validator(IsNotToNone(), IsOver(1))
	parameter = 1
	try:
		parameter = validator(parameter)  # expect true
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)
	else:
		print('{} is not empty, number and over 1'.format(parameter))

	# Validate Integer
	validator = Validator(
		IsNotToNone(),
		IsInteger(IsOver(0))
	)

	try:
		print('parameter is {}'.format(validator(1)))  # expect print 1
		print('parameter is {}'.format(validator(0)))  # expect raise (TypeError, ValueError)
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)

	# Validate Float
	validator = Validator(
		IsNotToNone(),
		IsFloat(IsOver(0))
	)

	try:
		print('parameter is {}'.format(validator(1.0)))  # expect print 1.0
		print('parameter is {}'.format(validator(3)))  # expect raise (TypeError, ValueError)
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)

	# Validate String
	validator = Validator(
		IsNotToNone(),
		IsNotEmpty(),
		IsString(IsIn('HEO', 'CHOI', 'HONG', 'KIM', 'BANG'))
	)

	try:
		print('parameter is {}'.format(validator('HEO')))  # expect print '허용선'
		print('parameter is {}'.format(validator('LEE')))  # expect raise (TypeError, ValueError)
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)

	# Validate List or Tuple
	validator = Validator(
		IsNotToNone(
			IsArray(
				IsNotEmpty(),
				IsElementOf(
					IsOver(0),
				)
			)
		),
	)

	parameter = []
	try:
		parameter = validator(parameter)  # expect false
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)
	else:
		print('{} is listable, not empty and all elements are over 0'.format(parameter))

	parameter = [0, 1, 2, 3]
	try:
		parameter = validator(parameter)  # expect false
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)
	else:
		print('{} is listable, not empty and all elements are over 0'.format(parameter))

	parameter = [1, 2, 3]
	try:
		parameter = validator(parameter)  # expect true
	except (TypeError, ValueError) as e:
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
		IsDictionary(
			IsRequiredInDictionary('a', 'b', 'c', 'd'),
			IsMappingOfDictionary({
				'a': Validator(IsNotToNone()),
				'b': Validator(IsNotToNone(), IsEqualTo(2)),
				'c': Validator(IsNotToNone(), IsIn(3, 4, 5, 6, 7, 8)),
				'd': Validator(SetDefault(4)),
				'e': Validator(IsNotToNone(IsArray(IsElementOf(IsOver(3))))),
				'f': Validator(IsDictionary(
					IsNotEmpty(),
					IsRequiredInDictionary('a', 'b'),
					IsMappingOfDictionary({
						'a': (IsNotToNone()),
						'b': (IsNotToNone(), IsOver(9)),
					})
				)),
			})
		)
	)
	try:
		parameter = validator(parameter)
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)
	else:
		print('{} is objectable, not empty and all validates of elements are ok'.format(parameter))

	# validate DataObject
	@dataclass
	class DataObject:
		a: bool
		b: int
		c: float
		d: str
		e: list
		f: dict
	_ = DataObject(
		a=True,
		b=1,
		c=1.0,
		d='1',
		e=[1],
		f={'a': 1, 'b': 1.0, 'c': 'str'},
	)
	va = Validator(
		IsDataObject(
			IsRequiredInDataObject('a', 'b', 'c', 'd', 'e', 'f'),
			IsMappingOfDataObject({
				'a': Validator(IsBool()),
				'b': Validator(IsInteger(IsIn(1, 2, 3))),
				'c': Validator(IsFloat(IsGreaterEqualTo(2))),
				'd': Validator(IsString()),
				'e': Validator(IsArray()),
				'f': Validator(IsDictionary(
					IsRequiredInDictionary('a', 'b'),
					IsMappingOfDictionary({
						'a': IsInteger(),
						'b': IsFloat(),
					})
				)),
			})
		)
	)
	_ = va(_)
	print(_)

	# Test Decorator with Function
	@Validate({
		'a': IsNotToNone(),
		'b': (IsNotToNone(), IsGreaterEqualTo(0)),
		'c': IsNotToNone(),
		'd': (IsNotToNone(), IsLessEqualTo(10)),
		'e': (IsArray(IsNotEmpty(), IsElementOf(IsLessThan(5)))),
		'f': IsDictionary(
			IsNotEmpty(),
			IsRequiredInDictionary('a', 'b'),
			IsMappingOfDictionary({
				'a': (IsNotToNone(), IsGreaterThan(0), IsLessThan(5)),
			})
		),
		'const': SetDefault(3),
	})
	def foo(a, b, c, d, e, f, const=None):
		return round((a + b + c + d) * sum(e) / sum(f.values()) % const)

	try:
		ret = foo(1, 2, 3, d=4, e=(1, 2, 3), f={'a': 2, 'b': 1})
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)
	else:
		print('foo returned {}'.format(ret))

	# Test Decorator with Method of Class
	class A:
		@Validate({
			'a': IsNotToNone(),
			'b': (IsNotToNone(), IsGreaterEqualTo(0)),
			'c': IsNotToNone(),
			'd': (IsNotToNone(), IsLessEqualTo(10)),
			'e': (IsArray(IsNotEmpty(), IsElementOf(IsLessThan(5)))),
			'f': IsDictionary(
				IsNotEmpty(),
				IsMappingOfDictionary({
					'a': (IsNotToNone(), IsGreaterThan(0), IsLessThan(5)),
				})
			),
			'const': SetDefault(3),
		})
		def foo(self, a, b, c, d, e, f, const=None):
			return round((a + b + c + d) * sum(e) / sum(f.values()) % const)

	try:
		a = A()
		ret = a.foo(1, 2, 3, d=4, e=(1, 2, 3), f={'a': 2, 'b': 1})
	except (TypeError, ValueError) as e:
		print(str(e), file=stderr)
	else:
		print('A.foo returned {}'.format(ret))
