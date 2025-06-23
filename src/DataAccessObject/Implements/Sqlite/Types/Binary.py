# -*- coding: utf-8 -*-

from ..Type import Type
from ..Function import Function

from Liquirizia.DataModel import Handler
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import (
	IsByteString,
)

from typing import Union

__all__ = (
	'Binary'
)


class Binary(Type, typestr='BLOB'):
	def __init__(
			self, 
			name: str, 
			va: Validator = Validator(IsByteString()),
			fn: Handler = None,
			null: bool = False,
			default: Union[bytes, Function] = None,
			description: str = None,
		):
		super().__init__(
			key=name, 
			type=bytes,
			va=va,
			fn=fn,
			null=null,
			default=str(default) if isinstance(default, Function) else default,
			description=description,
		)
		return
