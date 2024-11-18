# -*- coding: utf-8 -*-

from Liquirizia.DataModel import (
	Model,
	Value, 
	Handler,
)
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *

from Liquirizia.Util import PrettyPrint

from typing import Optional


class Changed(Handler):
	def __call__(self, m, o, v, pv):
		print('{} of {} is changed {} to {}'.format(o.name, m.__class__.__name__, pv, v))
		return
	

class SampleObject(Model, fn=Changed()):
	x: int = 0
	y: int = 0
	def move(self, weight: int = 1):
		self.x += weight
		self.y += weight
		return


# WITH DESCRIPTOR
class SampleModel(
	Model,
	description='Sample Model',
	fn=Changed()
):
	bOptionVal: bool = Value(va=Validator(IsToNone(IsTypeOf(bool))), fn=Changed())
	bOptionValWithNone: bool = Value(va=Validator(IsToNone(IsTypeOf(bool))), default=None, fn=Changed())
	bOptionValWithOutDescriptor: Optional[bool]
	bOptionValWithOutDescriptorWithDefault: Optional[bool] = True
	bVal: bool = Value(va=Validator(IsNotToNone(IsTypeOf(bool))), fn=Changed())
	bValWithNone: bool = Value(va=Validator(IsToNone(IsTypeOf(bool))), default=None, fn=Changed())
	bValWithDefault: bool = Value(va=Validator(IsTypeOf(bool)), default=True, fn=Changed())
	bValWithOutDescriptor: bool
	bValWithOutDescriptorWithNone: bool = None
	bValWithOutDescriptorWithDefault: bool = True

	iOptionVal: int = Value(va=Validator(IsToNone(IsTypeOf(int))), fn=Changed())
	iOptionValWithOutDescriptor: Optional[int]
	iOptionValWithOutDescriptorWithDefault: Optional[int] = 0
	iVal: int = Value(va=Validator(IsTypeOf(int)), fn=Changed())
	iValWithOutDescriptor: int
	iValWithOutDescriptorWithDefault: int = 0
	iValWithDefault: int = Value(va=Validator(IsTypeOf(int)), default=9, fn=Changed())

	fOptionVal: float = Value(va=Validator(IsToNone(IsTypeOf(float))), fn=Changed())
	fOptionValWithOutDescriptor: Optional[float]
	fOptionValWithOutDescriptorWithDefault: Optional[float] = 0.0
	fVal: float = Value(va=Validator(IsTypeOf(float)), fn=Changed())
	fValWithOutDescriptor: float
	fValWithOutDescriptorWithDefault: float = 0.0
	fValWithDefault: float = Value(va=Validator(IsTypeOf(float)), default=9.9, fn=Changed())

	sOptionVal: str = Value(va=Validator(IsToNone(IsTypeOf(str))), fn=Changed())
	sOptionValWithOutDescriptor: Optional[str]
	sOptionValWithOutDescriptorWithDefault: Optional[str] = 'ABC' 
	sVal: str = Value(va=Validator(IsTypeOf(str)), fn=Changed())
	sValWithOutDescriptor: str
	sValWithOutDescriptorWithDefault: str = 'DEF'
	sValWithDefault: str = Value(va=Validator(IsTypeOf(str)), default='STR', fn=Changed())

	liOptionVal: list = Value(va=Validator(IsToNone(IsTypeOf(list))), fn=Changed())
	liOptionValWithOutDescriptor: Optional[list]
	liOptionValWithOutDescriptorWithDefault: Optional[list] = [1,2,3]
	liVal: list = Value(va=Validator(IsTypeOf(list)), fn=Changed())
	liValWithOutDescriptor: list
	liValWithOutDescriptorWithDefault: list = [4,5,6]
	liValWithDefault: list = Value(va=Validator(IsTypeOf(list)), default=[9,8,7], fn=Changed())

	tuOptionVal: tuple = Value(va=Validator(IsToNone(IsTypeOf(tuple))), fn=Changed())
	tuOptionValWithOutDescriptor: Optional[tuple]
	tuOptionValWithOutDescriptorWithDefault: Optional[tuple] = (1,2,3)
	tuVal: tuple = Value(va=Validator(IsTypeOf(tuple)), fn=Changed())
	tuValWithOutDescriptor: tuple
	tuValWithOutDescriptorWithDefault: tuple = (4,5,6)
	tuValWithDefault: tuple = Value(va=Validator(IsTypeOf(tuple)), default=(9,8,7), fn=Changed())

	setOptionVal: set = Value(va=Validator(IsToNone(IsTypeOf(set))), fn=Changed())
	setOptionValWithOutDescriptor: Optional[set]
	setOptionValWithOutDescriptorWithDefault: Optional[set] = {1,2,3}
	setVal: set = Value(va=Validator(IsTypeOf(set)), fn=Changed())
	setValWithOutDescriptor: set
	setValWithOutDescriptorWithDefault: set = {4,5,6}
	setValWithDefault: set = Value(va=Validator(IsTypeOf(set)), default={9,8,7}, fn=Changed())

	dictOptionVal: dict = Value(va=Validator(IsToNone(IsTypeOf(dict))), fn=Changed())
	dictOptionValWithOutDescriptor: Optional[dict]
	dictOptionValWithOutDescriptorWithDefault: Optional[dict] = {'a':False, 'b': 1, 'c': 2.0, 'd': 'str'}
	dictVal: dict = Value(va=Validator(IsTypeOf(dict)), fn=Changed())
	dictValWithOutDescriptor: dict
	dictValWithOutDescriptorWithDefault: dict = {'a':False, 'b': 1, 'c': 2.0, 'd': 'str'}
	dictValWithDefault: dict = Value(va=Validator(IsTypeOf(dict)), default={'a':False, 'b': 1, 'c': 2.0, 'd': 'str'}, fn=Changed())

	oOptionVal: SampleObject = Value(va=Validator(IsToNone(IsTypeOf(SampleObject))), fn=Changed())
	oOptionValWithOutDescriptor: Optional[SampleObject]
	oOptionValWithOutDescriptorWithDefault: Optional[SampleObject] = SampleObject(x=1,y=2)
	oVal: SampleObject = Value(va=Validator(IsTypeOf(SampleObject)), fn=Changed())
	oValWithOutDescriptor: SampleObject
	oValWithOutDescriptorWithDefault: SampleObject = SampleObject(x=2,y=3)
	oValWithDefault: SampleObject = Value(va=Validator(IsTypeOf(SampleObject)), default=SampleObject(x=3,y=4), fn=Changed())


_ = SampleModel(
	bVal=False,
	bValWithOutDescriptor=False,
	iVal=1,
	iValWithOutDescriptor=2,
	fVal=3.1,
	fValWithOutDescriptor=4.2,
	sVal='abc',
	sValWithOutDescriptor='def',
	liVal=[1,2,3],
	liValWithOutDescriptor=[4,5,6],
	tuVal=(1,2,3),
	tuValWithOutDescriptor=(4,5,6),
	setVal={1,2,2},
	setValWithOutDescriptor={4,5,5},
	dictVal={'a':False, 'b': 1, 'c': 2.0, 'd': 'str'},
	dictValWithOutDescriptor={'a':False, 'b': 1, 'c': 2.0, 'd': 'str'},
	oVal=SampleObject(x=4,y=5),
	oValWithOutDescriptor=SampleObject(x=6,y=7),
)

PrettyPrint(_, indent=2)

_.bOptionVal = False
_.bOptionValWithOutDescriptor = True
_.bOptionValWithOutDescriptorWithDefault = False
_.bVal = True
_.bValWithOutDescriptor = True
_.bValWithOutDescriptorWithDefault = False
_.bOptionVal = None
_.bOptionValWithOutDescriptor = None
_.bOptionValWithOutDescriptorWithDefault = None

_.iOptionVal = 1
_.iOptionValWithOutDescriptor = 2
_.iOptionValWithOutDescriptorWithDefault = 3
_.iVal = 4
_.iValWithOutDescriptor = 5
_.iValWithOutDescriptorWithDefault = 6
_.iOptionVal = None
_.iOptionValWithOutDescriptor = None
_.iOptionValWithOutDescriptorWithDefault = None

_.fOptionVal = 1.1
_.fOptionValWithOutDescriptor = 2.2
_.fOptionValWithOutDescriptorWithDefault = 3.3
_.fVal = 4.4
_.fValWithOutDescriptor = 5.5
_.fValWithOutDescriptorWithDefault = 6.6
_.fOptionVal = None
_.fOptionValWithOutDescriptor = None
_.fOptionValWithOutDescriptorWithDefault = None

_.sOptionVal = 'abc'
_.sOptionValWithOutDescriptor = 'def'
_.sOptionValWithOutDescriptorWithDefault = 'ghi'
_.sVal = 'jkl'
_.sValWithOutDescriptor = 'mno'
_.sValWithOutDescriptorWithDefault = 'pqr'
_.sOptionVal = None
_.sOptionValWithOutDescriptor = None
_.sOptionValWithOutDescriptorWithDefault = None

_.liOptionVal = [1,2,3]
_.liOptionValWithOutDescriptor = [4,5,6]
_.liOptionValWithOutDescriptorWithDefault = [7,8,9]
_.liVal = [10,11,12]
_.liValWithOutDescriptor = [13,14,15]
_.liValWithOutDescriptorWithDefault = [16,17,18]
_.liOptionVal = None
_.liOptionValWithOutDescriptor = None
_.liOptionValWithOutDescriptorWithDefault = None

_.tuOptionVal = (1,2,3)
_.tuOptionValWithOutDescriptor = (4,5,6)
_.tuOptionValWithOutDescriptorWithDefault = (7,8,9)
_.tuVal = (10,11,12)
_.tuValWithOutDescriptor = (13,14,15)
_.tuValWithOutDescriptorWithDefault = (16,17,18)
_.tuOptionVal = None
_.tuOptionValWithOutDescriptor = None
_.tuOptionValWithOutDescriptorWithDefault = None

PrettyPrint(_, indent=2)
