# -*- coding: utf-8 -*-

from ..Type import Type
from ..Function import Function

from Liquirizia.DataModel import Handler

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import (
	IsToNone,
	IsNotToNone,
	IsInteger,
	IsFloat,
	ToInteger,
	ToFloat,
)


from typing import Union, Tuple, List

__all__ = (
	'Integer',
	'Float',
)


class Integer(Type, typestr='INTEGER'):
	def __init__(
			self, 
			name: str, 
			null: bool = False,
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
			default=str(default) if isinstance(default, Function) else default,
			description=description,
			va=va,
			fn=fn,
		)
		return


class Float(Type, typestr='REAL'):
	def __init__(
			self, 
			name: str, 
			null: bool = False,
			default: Union[int, Function] = None,
			description: str = None,
			va: Validator = None,
			fn: Handler = None,
		):
		if not va:
			if null:
				va = Validator(IsToNone(IsFloat()))
			else:
				va = Validator(IsNotToNone(IsFloat()))
		super().__init__(
			key=name, 
			type=self.typestr,
			null=null,
			default=str(default) if isinstance(default, Function) else default,
			description=description,
			va=va,
			fn=fn,
		)
		return
