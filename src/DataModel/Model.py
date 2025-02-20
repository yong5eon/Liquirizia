# -*- coding: utf-8 -*-

from .Value import Value
from .Format import Object
from .Handler import Handler

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import (
	IsToNone,
	IsNotToNone,
	IsTypeOf,
	Any as IsAny,
)
from Liquirizia.Validator.Patterns.Array import (
	IsElementOf,
)
from Liquirizia.Validator.Patterns.Dictionary import (
	IsKeyOf,
	IsValueOf,
)

from collections import OrderedDict

from typing import (
	get_origin,
	get_args,
	Any,
	Type,
	Union,
)

# TODO : support UnionType in 3.8
# from types import UnionType

__all__ = (
	'Model'
)


class ModelCreator(type):
	def __init__(self, typename, bases, namespace, *args, **kwargs):
		super().__init__(typename, bases, namespace, *args, **kwargs)
		try:
			for k, t in self.__annotations__.items():
				v = self.__dict__[k] if k in self.__dict__.keys() else None
				if not isinstance(v, Value):
					v = self.__value__(k, t, v)
					setattr(self, k, v)
		except Exception as e:
			pass
		self.__mapper__ = OrderedDict()
		self.__description__ = None
		self.__fmt__ = None
		for k, v in self.__dict__.items():
			if not isinstance(v, Value): continue
			v.__set_name__(self, k)
			self.__mapper__[k] = v
		return
	def __repr__(cls):
		return cls.__model__


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
				v.__set__(self, v.default, init=True)
		return
	
	def __init_subclass__(cls, name: str = None, description: str = None, format: Object = None, fn: Handler = None):
		cls.__model__ = name if name else cls.__name__
		cls.__description__ = description
		cls.__fmt__ = format
		cls.__callback__ = fn
		return super().__init_subclass__()

	def __repr__(self):
		_ = []
		for k, t in self.__mapper__.items():
			_.append('{}={}'.format(k, getattr(self, k)))
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(_)
		)
	
	def __setattr__(self, name, value):
		if name in ('__properties__'): return super().__setattr__(name, value)
		if name not in self.__mapper__.keys():
			raise ValueError('{} is not member of {}'.format(name, self.__class__.__name__))
		return super().__setattr__(name, value)

	@classmethod
	def __value__(cls, k: str, t: Type, v: Any):
		hv = k in cls.__dict__.keys()
		vaps = cls.__vaps__(t, v, hv)
		v = Value(
			va=Validator(vaps) if vaps else Validator(),
			default=v,
		)
		return v

	@classmethod
	def __vaps__(cls, t, v: Any, hv: bool):
		targs = get_args(t)
		t = get_origin(t) if get_origin(t) else t
		if t in (bool, int, float, str, bytes):
			if hv and v is None:
				return IsToNone(IsTypeOf(t))
			else:
				return IsNotToNone(IsTypeOf(t))
		if t in (set, frozenset, tuple, list, bytearray):
			vaps = []
			for ta in targs:
				vaps.append(cls.__vaps__(ta, v, hv))
			return IsToNone(IsTypeOf(t, IsElementOf(*vaps))) if hv and v is None else IsNotToNone(IsTypeOf(t, IsElementOf(*vaps)))
		if t is dict:
			vaps = []
			if len(targs):
				kvaps = cls.__vaps__(targs[0], None, False)
				vaps.append(IsKeyOf(kvaps,))
			if len(targs) > 1:
				vvaps = cls.__vaps__(targs[1], None, False)
				vaps.append(IsValueOf(vvaps,))
			return IsToNone(IsTypeOf(t, vaps)) if hv and v is None else IsNotToNone(IsTypeOf(t, vaps))
		# TODO : if want to do special for Model

		# TODO : support UnionType in 3.8
		# if t in (Union, UnionType):
		if t in (Union,):
			return cls.__vaps_union__(targs, v, hv)
		# raise TypeError('{} is not support type in Model'.format(t))
		return IsToNone(IsTypeOf(t)) if hv and v is None else IsNotToNone(IsTypeOf(t))

	@classmethod
	def __vaps_union__(cls, types: set, v: Any, hv: bool):
		ts = []
		for t in types:
			if t is type(None):
				v = None
				hv = True
				continue
			ts.append(t)
		if len(ts) == 0:
			return ()
		if len(ts) == 1:
			return cls.__vaps__(ts[0], v, hv)
		vaps = []
		for t in ts:
			vaps.append(cls.__vaps__(t, v, hv))
		return IsAny(*vaps)

	@classmethod
	def ToString(cls): return cls.__model__
