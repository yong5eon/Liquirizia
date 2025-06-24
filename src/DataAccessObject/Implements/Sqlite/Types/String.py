# -*- coding: utf-8 -*-

from ..Type import Type
from ..Function import Function

from Liquirizia.DataModel import Handler
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import (
	IsString
)

from typing import Union

__all__ = (
	'Text'
)


class Text(Type, typestr='TEXT'):
	def __init__(
			self, 
			name: str, 
			va: Validator = Validator(IsString()),
			fn: Handler = None,
			null: bool = False,
			default: Union[str, Function] = None,
			description: str = None,
		):
		super().__init__(
			key=name, 
			type=str,
			va=va,
			fn=fn,
			null=null,
			default=str(default) if isinstance(default, Function) else '\'{}\''.format(default),
			description=description,
		)
		return
