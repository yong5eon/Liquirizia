# -*- coding: utf-8 -*-

from Liquirizia.DataModelObject import Model, Type
from Liquirizia.DataModelObject.Mutable import DataModelObject
from Liquirizia.DataModelObject.Mutable.Types import *

from Liquirizia.Validator.Patterns import *

from Liquirizia.Validator import Pattern

from random import randint
from datetime import datetime


class IsStringFixedLength(Pattern):
	def __init__(self, length):
		self.length = length
		return

	def __call__(self, parameter):
		if len(parameter) != self.length:
			raise RuntimeError('{} is must be {} length'.format(parameter, self.length))
		return parameter

@Model(
	typeBool=Type(Bool),
	typeInteger=Type(Integer),
	typeFloat=Type(Float),
	typeString=Type(String),
	typeDateTime=Type(DateTime),
	typeList=Type(List),
	typeTuple=Type(Tuple),
	typeDictionary=Type(Dictionary),
)
class SampleModel(DataModelObject):
	def __init__(
		self,
		typeBool,
		typeInteger,
		typeFloat,
		typeString,
		typeDateTime,
		typeList,
		typeTuple,
		typeDictionary,
	):
		super(SampleModel, self).__init__(
			typeBool=typeBool,
			typeInteger=typeInteger,
			typeFloat=typeFloat,
			typeString=typeString,
			typeDateTime=typeDateTime,
			typeList=typeList,
			typeTuple=typeTuple,
			typeDictionary=typeDictionary,
		)
		pass


if __name__ == '__main__':

	val = SampleModel(
		True,
		1,
		0.1,
		'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
		datetime.now(),
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
		(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
		{
			'a': 1,
			'b': 2,
			'c': 3,
		},
	)

	print(val)

	try:
		val['typeBool'] = False
		val['typeInteger'] = 9
	except Exception as e:
		print(str(e))

	print(val)

