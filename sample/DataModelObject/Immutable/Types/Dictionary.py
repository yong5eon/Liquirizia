# -*- coding: utf-8 -*-

from Liquirizia.DataModelObject.Immutable.Types import *

from Liquirizia.Validator.Patterns import *

from sys import stderr


if __name__ == '__main__':

	# try with internal type
	try:
		print({
			'a': 1,
			'b': 3.0,
			'c': 'B',
			'd': [1, 2, 3],
			'e': {
				'ea': 1,
				'eb': 3.0,
				'ec': 'C'
			}
		})
		a = Dictionary({
			'a': 1,
			'b': 3.0,
			'c': 'B',
			'd': [1, 2, 3],
			'e': {
				'ea': 1,
				'eb': 3.0,
				'ec': 'C'
			}
		}, {
			'a': IsInteger(IsRange(0, 10)),
			'b': IsFloat(IsGreaterEqualTo(2)),
			'c': IsString(IsIn('A', 'B', 'C')),
			'd': IsListable(IsRange(1, 4)),
			'e': IsDictionary({
				'ea': IsRange(0, 10),
				'eb': IsGreaterEqualTo(2),
				'ec': IsString(IsIn('A', 'B', 'C')),
			})
		})
		print(len(a))
		print(a)
		for v in a.keys():
			print(a[v])
		for i, v in a.items():
			print('{} : {}'.format(i, v))
		a['a'] = 3  # expected RuntimeError
		for v in a.keys():
			print(a[v])
		for i, v in a.items():
			print('{} : {}'.format(i, v))
	except Exception as e:
		print(str(e), file=stderr)

	# try with data type object
	try:
		a = Dictionary({
			'a': Integer(1, IsRange(0, 10)),
			'b': Float(3.0, IsGreaterEqualTo(2)),
			'c': String('B', IsIn('A', 'B', 'C')),
			'd': List((1, 2, 3), IsRange(1, 4)),
			'e': Dictionary({
				'ea': Integer(1, IsRange(0, 10)),
				'eb': Float(3.0, IsGreaterEqualTo(2)),
				'ec': String('C', IsIn('A', 'B', 'C')),
			})
		})
		print(len(a))
		print(a)
		for v in a.keys():
			print(a[v])
		for i, v in a.items():
			print('{} : {}'.format(i, v))
		a['a'] = 3  # expected RuntimeError
		for v in a.keys():
			print(a[v])
		for i, v in a.items():
			print('{} : {}'.format(i, v))
	except Exception as e:
		print(str(e), file=stderr)
