# -*- coding: utf-8 -*-

from ..Type import Type
from ..Function import Function

from Liquirizia.DataModel import Handler

from Liquirizia.Validator import Validator, Pattern
from Liquirizia.Validator.Patterns import (
	IsToNone,
	IsNotToNone,
	IsDateTime,
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
				if isinstance(parameter, str):
					return datetime.fromisoformat(parameter)
				return parameter
		if not va:
			if null:
				va = Validator(IsToNone(StrToDateTime(), IsDateTime()))
			else:
				va = Validator(IsNotToNone(StrToDateTime(), IsDateTime()))
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
