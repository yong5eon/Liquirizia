# -*- coding: utf-8 -*-

from ..Type import Type
from ..Function import Function

from Liquirizia.DataModel import Handler
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import (
	IsInteger,
	IsFloat,
)


from typing import Union

__all__ = (
	'Integer',
	'Float',
)


class Integer(Type, typestr='INTEGER'):
	def __init__(
			self, 
			name: str, 
			va: Validator = Validator(IsInteger()),
			fn: Handler = None,
			null: bool = False,
			default: Union[int, Function] = None,
			description: str = None,
		):
		super().__init__(
			key=name, 
			type=int,
			va=va,
			fn=fn,
			null=null,
			default=str(default) if isinstance(default, Function) else default,
			description=description,
		)
		return


class Float(Type, typestr='REAL'):
	def __init__(
		self, 
		name: str, 
		va: Validator = Validator(IsFloat()),
		fn: Handler = None,
		null: bool = False,
		default: Union[int, Function] = None,
		description: str = None,
	):
		super().__init__(
			key=name, 
			type=float,
			va=va,
			fn=fn,
			null=null,
			default=str(default) if isinstance(default, Function) else default,
			description=description,
		)
		return
