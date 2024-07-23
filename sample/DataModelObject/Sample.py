# -*- coding: utf-8 -*-

from Liquirizia.DataModelObject import (
	DataModelObject,
	DataAttributeObject, 
	DataObjectHandler,
)
from Liquirizia.Validator import Validator, Pattern
from Liquirizia.Validator.Patterns import *

from Liquirizia.Test import (
	Case,
	ASSERT,
)
from Liquirizia.Test.Patterns import (
	IsEqualTo as AssertEqualTo,
	IsNotEqualTo as AssertNotEqualTo,
	IsTrue as AssertTrue,
	IsFalse as AssertFalse,
	IsExceptionWith as AssertExceptionWith,
)

from Liquirizia.Util import PrettyPrint, PrettyDump

from random import random, randrange
from sys import stderr


class DataModelPropertiesHandler(DataObjectHandler):
	def __call__(self, o : DataModelObject, n : str, v : any, p : any):
		print('DataModelProperties changed {} from {} to {} in {}'.format(n, p, v, PrettyDump(o)))
		return


class DataModelProperties(DataModelObject):
	typeInteger = DataAttributeObject(Validator(IsInteger(IsRange(0, 10, 3))), fn=DataModelPropertiesHandler())
	typeFloat = DataAttributeObject(Validator(IsFloat(IsRange(1, 10, 3))), fn=DataModelPropertiesHandler())


class DataModelHandler(DataObjectHandler):
	def __call__(self, o : DataModelObject, n : str, v : any, p : any):
		print('DataModel changed {} from {} to {} in {}'.format(n, p, v, PrettyDump(o)))
		return


class IsDataModelProperties(Pattern):
	def __call__(self, parameter):
		if not isinstance(parameter, DataModelProperties):
			raise TypeError('{} is not DataModelObject'.format(parameter.__class__.__name__))
		return parameter


class DataModel(DataModelObject):
	typeBool = DataAttributeObject(Validator(IsBool(IsEqualTo(True))), fn=DataModelHandler())
	typeInteger = DataAttributeObject(Validator(IsInteger(IsRange(0, 10, 2))), fn=DataModelHandler())
	typeFloat = DataAttributeObject(Validator(IsFloat(IsRange(1, 10, 2))), fn=DataModelHandler())
	typeString = DataAttributeObject(Validator(IsString(IsIn('Hello', 'Hi'))), fn=DataModelHandler())
	typeList = DataAttributeObject(Validator(IsList(IsElementOf(IsInteger(IsRange(0, 10))))), fn=DataModelHandler())
	typeListOfList = DataAttributeObject(Validator(IsAbleToNone(IsList(IsElementOf(IsList(IsElementOf(IsRange(0, 10))))))), fn=DataModelHandler())
	typeListOfDict = DataAttributeObject(
		Validator(IsAbleToNone(IsList(IsElementOf(IsDictionary(
			IsRequiredIn('typeInteger', 'typeFloat'),
			IsMappingOf({
				'typeInteger': Validator(IsInteger(IsIn(1,2,3))),
				'typeFloat': Validator(IsFloat(IsRange(0, 5))),
				'typeList': Validator(IsList(IsElementOf(IsIn('KIM', 'LEE', 'PARK', 'CHOI', 'HEO'))))
			})
		))))),
		fn=DataModelHandler()
	)
	typeDict = DataAttributeObject(Validator(IsDictionary(
		IsMappingOf({
			'typeList': Validator(IsList(IsElementOf(IsIn('KIM', 'BANG', 'JEONG', 'HEO'))))
		})
	)), fn=DataModelHandler())
	typeDataModel = DataAttributeObject(Validator(IsDataModelProperties()), fn=DataModelHandler())
	typeListOfDataModel = DataAttributeObject(Validator(IsList(IsElementOf(IsDataModelProperties()))), fn=DataModelHandler())

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

_.typeInteger = 0
_.typeInteger += 2
_.typeInteger = 8

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
		pass

_.typeListOfList = []
_.typeListOfList.append([])
_.typeListOfList[0].append(1.0)
_.typeListOfList[0].append(9.0)
_.typeListOfList[0][0] = 3
_.typeListOfList[0][1] = 2

_.typeList2 = []
_.typeList2.append(1)
_.typeList2.append(2)
_.typeList2.append(4)

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
