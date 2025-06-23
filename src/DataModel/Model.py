# -*- coding: utf-8 -*-

from .Value import Value, Parameters, MISSING
from .Handler import Handler

from collections import OrderedDict
from decimal import Decimal
from datetime import datetime, date, time
from types import NoneType
from typing import (
	get_origin,
	get_args,
	Any,
	Type,
	Union,
	Annotated,
	Dict,
)

__all__ = (
	'Model'
)


class ModelCreator(type):
	def __init__(self, typename, bases, namespace, *args, **kwargs):
		super().__init__(typename, bases, namespace, *args, **kwargs)
		for k, t in self.__annotations__.items():
			v = self.__dict__[k] if k in self.__dict__.keys() else MISSING
			if not isinstance(v, Value):
				v = self.attr(t, v)
				setattr(self, k, v)
		self.__mapper__: Dict[str, Value] = OrderedDict()
		for k, v in self.__dict__.items():
			if not isinstance(v, Value): continue
			v.__set_name__(self, k)
			self.__mapper__[k] = v
		return
	def __repr__(cls):
		return cls.__model__
	def attr(self, t: Type, default: Any, desc: Parameters = None):
		origin = get_origin(t)
		if origin == Annotated:
			args = get_args(t)
			t = args[0]
			if isinstance(args[1], str):
				return self.attr(
					t,
					default,
					Parameters(
						description=args[1],
					),
				)
			elif isinstance(args[1], dict):
				return self.attr(
					t,
					default,
					Parameters(**args[1]),
				)
			else:
				raise TypeError('{} must be dict or string'.format(args[1]))
		elif origin == Union:
			args = get_args(t)
			t = args[0]
			if len(args) > 2:
				raise TypeError('Not supported Union type with types')
			if len(args) == 2:
				if isinstance(args[1], type) and args[1] is not NoneType:
					raise TypeError('Not supported Union type with types')
				if args[1] is NoneType and default is MISSING:
					default = None
			return self.attr(t, default, desc)
		else:
			t = origin if origin else t
			PATTERNS = [
				bool,
				int,
				float,
				str,
				list,
				tuple,
				set,
				dict,
				bytes,
				bytearray,
				Decimal,
				datetime,
				date,
				time,
			]
			if t not in PATTERNS:
				raise TypeError('Not supported type {}'.format(t))
			v = Value(
				type=t,
				va=desc.va if desc else None,
				fn=desc.fn if desc else None,
				default=default,
				min=desc.min if desc else None,
				max=desc.max if desc else None,
				enum=desc.enum if desc else None,
				format=desc.format if desc else None,
				description=desc.description if desc else None,
			)
		return v


class Model(object, metaclass=ModelCreator):
	"""Abstract Model Class of Data Model"""

	def __new__(cls, **kwargs):
		o = object.__new__(cls)
		o.__properties__ = {}
		return o
	
	def __init__(self, **kwargs):
		for k, v in self.__mapper__.items():
			if k in kwargs.keys():
				v.__set__(self, kwargs[k], init=True)
			else:
				if v.default is MISSING and v.required:	
					raise ValueError('{} is required in {}'.format(k, self.__class__.__name__))
				v.__set__(self, v.default, init=True)
		return
	
	def __init_subclass__(cls, name: str = None, fn: Handler = None, description: str = None):
		cls.__model__ = name if name else cls.__name__
		cls.__callback__ = fn
		cls.__description__ = description
		return super().__init_subclass__()

	def __repr__(self):
		_ = []
		for k, t in self.__mapper__.items():
			v = getattr(self, k)
			_.append('{}={}'.format(k, '\'{}\''.format(v) if isinstance(v, str) else repr(v)))
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(_)
		)
	
	def __setattr__(self, name, value):
		if name in ('__properties__'): return super().__setattr__(name, value)
		if name not in self.__mapper__.keys():
			raise ValueError('{} is not member of {}'.format(name, self.__class__.__name__))
		return super().__setattr__(name, value)

	def __eq__(self, value):
		if not isinstance(value, Model):
			return False
		return self.__properties__.__eq__(value.__properties__)
	
	def __ne__(self, value):
		if not isinstance(value, Model):
			return True
		return self.__properties__.__ne__(value.__properties__)