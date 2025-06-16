# -*- coding: utf-8 -*-

from Liquirizia.Description import *
from Liquirizia.Utils import PrettyPrint

from dataclasses import dataclass, field

from typing import Optional, List, Dict, Union, Annotated


@dataclass
class Parameters:
	a: int
	b: int


@dataclass
class Query:
	a: int
	b: float
	c: str = None


@dataclass
class Content:
	a: int
	b: float


@dataclass
class Arguments:
	parameters: Parameters
	qs: Query
	content: Content = None

from datetime import datetime

@dataclass
class Data:
	message: str
	args: Arguments
	ret: float
	timestamp: datetime

@dataclass
class Sample:
	bVal: bool
	iVal: int
	fVal: float
	sVal: str
	liVal: list
	liValAnnotated: List[int]
	oVal: dict
	oValAnnotated: Dict[str, int]
	# optional
	bOptionalVal: Optional[bool]
	iOptionalVal: Optional[int]
	fOptionalVal: Optional[float]
	sOptionalVal: Optional[str]
	liOptionalVal: Optional[list]
	liOptionalValAnnotated: Optional[List[int]]
	oOptionalVal: Optional[dict]
	liOptionalValAnnotated: Optional[Dict[str, int]]
	# nullable
	bValNullable: bool = None
	iValNullable: int = None
	fValNullable: float = None
	sValNullable: str = None
	liValNullable: list = None
	liValAnnotatedNulllable: List[int] = None
	oValNullable: dict = None
	oValAnnotatedNullable: Dict[str, int] = None
	# has default
	bValDefault: bool = True
	iValDefault: int = 0
	fValDefault: float = 0.0
	sValDefault: str = ''
	liValDefault: list = field(default_factory=list)
	liValAnnotatedDefault: List[int] = field(default_factory=list)
	oValDefault: dict = field(default_factory=dict)
	oValAnnotatedDefault: Dict[str, int] = field(default_factory=dict)


@dataclass
class TestUnion:
	a: Annotated[Optional[int], '가', {'format': 'int64', 'min': 1000, 'max': 10000}]
	b: Annotated[Union[int, float], '나']
	c: Annotated[Union[int, float, bool], '다']
	d: Annotated[List[Union[int, float]], '라']
	e: Annotated[Dict[str, Union[int, float]], '마']
	f: Annotated[Optional[int], {'format': 'int32', 'min': 1000, 'max': 10000}, '아']
	g: Annotated[str, '바', {'enum': ('Y', 'N')}] = None
	h: Annotated[str, {'enum': ('Y', 'N')}, '??', '???'] = None 

if __name__ == '__main__':

	def typemapper(o):
		if o is datetime:
			return String, {'format': 'date-time'}
		return
	
	def typeencoder(o):
		if isinstance(o, datetime):
			return o.isoformat()
		raise TypeError('{} is not a supported type'.format(o.__class__.__name__))

	print('Schema')
	print('-' * 80)
	PrettyPrint(DumpSchema(ToSchema(Data, typedef=typemapper)))
	print('Object')
	print('-' * 80)
	PrettyPrint(ToObject(Data(
		message='Hello World',
		args=Arguments(
			parameters=Parameters(1, 2),
			qs=Query(1, 2.0),
			content=Content(1, 2.0)
		),
		ret=3.0,
		timestamp=datetime.now()
	), typeenc=typeencoder))

