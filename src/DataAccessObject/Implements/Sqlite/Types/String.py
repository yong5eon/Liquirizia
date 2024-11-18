# -*- coding: utf-8 -*-

from ..Type import Type
from ..Function import Function

from Liquirizia.DataModel import Handler
from Liquirizia.Validator import Validator, Pattern
from Liquirizia.Validator.Patterns import (
	IsToNone,
	IsNotToNone,
	IsString
)

from typing import Union, Tuple, List

__all__ = (
	'Text'
)


class Text(Type, typestr='TEXT'):
	def __init__(
			self, 
			name: str, 
			null: bool = False,
			default: Union[str, Function] = None,
			description: str = None,
			va: Validator = None,
			fn: Handler = None,
		):
		if not va:
			if null:
				va = Validator(IsToNone(IsString()))
			else:
				va = Validator(IsNotToNone(IsString()))
		super().__init__(
			key=name, 
			type=self.typestr,
			null=null,
			default=str(default) if isinstance(default, Function) else '\'{}\''.format(default),
			description=description,
			va=va,
			fn=fn,
		)
		return
