# -*- coding: utf-8 -*-

from Liquirizia.Test import *


from Liquirizia.DataModel import (
	Model,
	Attribute, 
	Handler,
)
from Liquirizia.Validator import Validator, Pattern
from Liquirizia.Validator.Patterns import *

from random import random, randrange
from sys import stderr


class DataModelPropertiesHandler(Handler):
	def __call__(self, o : Model, n : str, v : any, p : any):
		return


class DataModelProperties(Model):
	typeInteger = Attribute(Validator(IsInteger(IsRange(0, 10, 3))), fn=DataModelPropertiesHandler())
	typeFloat = Attribute(Validator(IsFloat(IsRange(1, 10, 3))), fn=DataModelPropertiesHandler())


class DataHandler(Handler):
	def __call__(self, o : Model, n : str, v : any, p : any):
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
	typeListOfList = Attribute(Validator(IsAbleToNone(IsList(IsElementOf(IsList(IsElementOf(IsRange(0, 10))))))), fn=DataHandler())
	typeListOfDict = Attribute(
		Validator(IsAbleToNone(IsList(IsElementOf(IsDictionary(
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


class TestDataModel(Case):

	@Order(0)
	def test_init(self):
		self._ = DataModel(
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
