# -*- coding: utf-8 -*-

from Liquirizia.Description import *
from Liquirizia.Utils import PrettyPrint

from dataclasses import dataclass, field

from typing import Optional, List, Dict

__all__ = (
	'FORMAT_ARGS',
	'FORMAT_DATA',
)


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


@dataclass
class Data:
	message: str
	args: Arguments
	ret: float


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


if __name__ == '__main__':

	_ = ToSchema(Data)
	PrettyPrint(DumpSchema(_))
