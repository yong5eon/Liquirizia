# -*- coding: utf-8 -*-

from ..Type import Type
from ..Function import Function

from Liquirizia.DataModel import Handler
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import (
	IsDateTime,
)

from datetime import datetime

from typing import Union

__all__ = (
	'DateTime',
	'Timestamp',
)


class IfStrOrTimestampToDateTime(IsDateTime):
	def __call__(self, parameter):
		if isinstance(parameter, str):
			parameter = datetime.fromisoformat(parameter)
		if isinstance(parameter, float):
			parameter = datetime.fromtimestamp(parameter)
		return super().__call__(parameter)


class DateTime(Type, typestr='DATETIME'):
	def __init__(
			self, 
			name: str, 
			va: Validator = Validator(IfStrOrTimestampToDateTime()),
			fn: Handler = None,
			null: bool = False,
			default: Union[datetime, Function] = None,
			description: str = None,
		):
		super().__init__(
			key=name, 
			va=va, 
			fn=fn,
			type=datetime,
			null=null,
			default=default,
			description=description,
		)
		return


class Timestamp(Type, typestr='TIMESTAMP'):
	def __init__(
			self, 
			name: str, 
			va: Validator = Validator(IfStrOrTimestampToDateTime()),
			fn: Handler = None,
			null: bool = False,
			default: Union[int, Function] = None,
			description: str = None,
		):
		super().__init__(
			key=name, 
			type=datetime,
			va=va, 
			fn=fn,
			null=null,
			default=default,
			description=description,
		)
		return
