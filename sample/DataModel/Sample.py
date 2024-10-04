# -*- coding: utf-8 -*-

from Liquirizia.DataModel import (
	Model,
	Attribute, 
	Handler,
)
from Liquirizia.Validator import Validator, Pattern
from Liquirizia.Validator.Patterns import *

from Liquirizia.Util import PrettyPrint, PrettyDump

from random import random, randrange
from sys import stderr


class DataModelPropertiesHandler(Handler):
	def __call__(
		self, 
		model,     # Model
		obj,       # Instance of Model
		attr,      # Attribute of Model
		value,     # Changed Value
		preValue,  # Previous Value
	):
		print('DataModelProperties changed {} from {} to {} in {}'.format(attr, value, preValue, obj))
		return


class DataModelProperties(Model):
	typeInteger = Attribute(Validator(IsInteger(IsRange(0, 10, 3))), fn=DataModelPropertiesHandler())
	typeFloat = Attribute(Validator(IsFloat(IsRange(1, 10, 3))), fn=DataModelPropertiesHandler())


class DataHandler(Handler):
	def __call__(
		self, 
		model,     # Model
		obj,       # Instance of Model
		attr,      # Attribute of Model
		value,     # Changed Value
		preValue,  # Previous Value
	):
		print('DataModel changed {} from {} to {} in {}'.format(attr, value, preValue, obj))
		return


class IsDataModelProperties(Pattern):
	def __call__(self, parameter):
		if not isinstance(parameter, DataModelProperties):
			raise TypeError('{} is not Model'.format(parameter.__class__.__name__))
		return parameter


class DataModel(Model):
	typeBool = Attribute(Validator(IsBool(IsEqualTo(True))), fn=DataHandler())
	typeInteger = Attribute(Validator(IsInteger(IsRange(0, 10, 2))), fn=DataHandler())
	typeFloat = Attribute(Validator(IsFloat(IsRange(1, 10, 2))), fn=DataHandler())
	typeString = Attribute(Validator(IsString(IsIn('Hello', 'Hi'))), fn=DataHandler())
	typeList = Attribute(Validator(IsList(IsElementOf(IsInteger(IsRange(0, 10))))), fn=DataHandler())
	typeListOfList = Attribute(Validator(IsToNone(IsList(IsElementOf(IsList(IsElementOf(IsRange(0, 10))))))), fn=DataHandler())
	typeListOfDict = Attribute(
		Validator(IsToNone(IsList(IsElementOf(IsDictionary(
			IsRequiredIn('typeInteger', 'typeFloat'),
			IsMappingOf({
				'typeInteger': Validator(IsInteger(IsIn(1,2,3))),
				'typeFloat': Validator(IsFloat(IsRange(0, 5))),
				'typeList': Validator(IsList(IsElementOf(IsIn('KIM', 'LEE', 'PARK', 'CHOI', 'HEO'))))
			})
		))))),
		fn=DataHandler()
	)
	typeDict = Attribute(Validator(IsDictionary(
		IsMappingOf({
			'typeList': Validator(IsList(IsElementOf(IsIn('KIM', 'BANG', 'JEONG', 'HEO'))))
		})
	)), fn=DataHandler())
	typeDataModel = Attribute(Validator(IsDataModelProperties()), fn=DataHandler())
	typeListOfDataModel = Attribute(Validator(IsList(IsElementOf(IsDataModelProperties()))), fn=DataHandler())

_ = DataModel(
	typeBool=True,
	typeInteger=0,
	typeFloat=1.0,
	typeString='Hello',
	typeList=[],
	typeDict={
		'typeList': ['KIM',]
	},
	typeListOfDict=[],
	typeDataModel=DataModelProperties(
		typeInteger=3,
		typeFloat=4.0
	),
	typeListOfDataModel = [
		DataModelProperties(
			typeInteger=3,
			typeFloat=7.0
		)
	]
)

PrettyPrint(_)

_.typeBool = True
isinstance(_.typeBool, bool)

_.typeInteger = 0
_.typeInteger += 2
_.typeInteger = 8
isinstance(_.typeInteger, int)

_.typeFloat = 1.0
_.typeFloat = 3.0

_.typeString = 'Hello'
_.typeString = 'Hi'

_.typeList = []

for v in range(0, 10):
	try:
		_.typeList.append(randrange(0, 20))
	except Exception as e:
		print('{}: {}'.format(e.__class__.__name__, str(e)), file=stderr)

for i, v in enumerate(_.typeList):
	try:
		_.typeList[i] = randrange(0, 20)
	except Exception as e:
		print('{}: {}'.format(e.__class__.__name__, str(e)), file=stderr)

_.typeListOfList = []
_.typeListOfList.append([])
_.typeListOfList[0].append(1.0)
_.typeListOfList[0].append(9.0)
_.typeListOfList[0][0] = 3
_.typeListOfList[0][1] = 2

_.typeListOfDict = []
_.typeListOfDict.append({
	'typeInteger': 1,
	'typeFloat': 2.0,
	'typeList': ['KIM', 'LEE', 'PARK']
})
_.typeListOfDict[0]['typeBool'] = True
_.typeListOfDict[0]['typeInteger'] = 2
_.typeListOfDict[0]['typeFloat'] = 4.0
_.typeListOfDict[0]['typeList'] = []
_.typeListOfDict[0]['typeList'].append('KIM')
_.typeListOfDict[0]['typeList'].append('HEO')

_.typeDict['typeList'].append('HEO')
_.typeDict['typeList'].append('BANG')

_.typeDataModel = DataModelProperties(
	typeInteger=3,
	typeFloat=1.0,
)

_.typeDataModel.typeInteger = 6
_.typeListOfDataModel[0].typeFloat = 4.0

PrettyPrint(_)
