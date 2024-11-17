# -*- coding: utf-8 -*-

from ..Type import Type
from ..Function import Function

from Liquirizia.DataModel import Handler

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import (
	IsToNone,
	IsNotToNone,
	IsByteArray,
	ToByteArray,
)

from typing import Union

__all__ = (
	'ByteArray'
)


class ByteArray(Type, typestr='BLOB'):
	def __init__(
			self, 
			name: str, 
			null: bool = False,
			default: Union[bytes, Function] = None,
			va: Validator = None,
			fn: Handler = None,
		):
		if not va:
			if null:
				va = Validator(IsToNone(ToByteArray(), IsByteArray()))
			else:
				va = Validator(IsNotToNone(ToByteArray(), IsByteArray()))
		super().__init__(
			key=name, 
			type=self.typestr,
			null=null,
			default=str(default) if isinstance(default, Function) else default,
			va=va,
			fn=fn,
		)
		return
