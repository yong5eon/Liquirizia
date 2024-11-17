# -*- coding: utf-8 -*-

from ..Type import Type
from ..Function import Function

from Liquirizia.DataModel import Handler

from Liquirizia.Validator import Validator, Pattern
from Liquirizia.Validator.Patterns import (
	IsToNone,
	IsNotToNone,
	IsDateTime,
	If,
	IsString,
	IsInteger,
)

from datetime import datetime

from typing import Union, Tuple, List

__all__ = (
	'DateTime',
	'Timestamp',
)


class DateTime(Type, typestr='DATETIME'):
	def __init__(
			self, 
			name: str, 
			null: bool = False,
			default: Union[datetime, Function] = None,
			description: str = None,
			va: Validator = None,
			fn: Handler = None,
		):
		class StrToDateTime(Pattern):
			def __call__(self, parameter):
				return datetime.fromisoformat(parameter)
		if not va:
			if null:
				va = Validator(IsToNone(If(IsString(StrToDateTime())), IsDateTime()))
			else:
				va = Validator(IsNotToNone(If(IsString(StrToDateTime())), IsDateTime()))
		super().__init__(
			key=name, 
			type=self.typestr,
			null=null,
			default=default,
			description=description,
			va=va, 
			fn=fn,
		)
		return


class Timestamp(Type, typestr='TIMESTAMP'):
	def __init__(
			self, 
			name: str, 
			null=False,
			default: Union[int, Function] = None,
			description: str = None,
			va: Validator = None,
			fn: Handler = None,
		):
		if not va:
			if null:
				va = Validator(IsToNone(IsInteger()))
			else:
				va = Validator(IsNotToNone(IsInteger()))
		super().__init__(
			key=name, 
			type=self.typestr,
			null=null,
			default=default,
			description=description,
			va=va, 
			fn=fn,
		)
		return
