# -*- coding: utf-8 -*-

from Liquirizia.Validator import Validator
from numpy.ma.extras import isin

from .Handler import Handler
from .Type import Type

from typing import Sequence, Type as T, Any, Union

__all__ = (
	'Value',
	'Parameters',
	'MISSING',
)

class MISSING_TYPE(object): pass
MISSING = MISSING_TYPE()

class Parameters(object):
	def __init__(
		self,
		va: Validator = None,
		fn: Handler = None,
		min: Any = None,
		max: Any = None,
		enum: Sequence[Any] = None,
		format: str = None,
		description: str = None,
	):
		self.va = va
		self.fn = fn
		self.min = min
		self.max = max
		self.enum = enum
		self.format = format
		self.description = description
		return

class Value(object):
	"""Value Class of Model"""

	def __init__(
		self,
		type: T,
		va: Validator = None,
		fn: Handler = None,
		default: Any = MISSING,
		min: Any = None,
		max: Any = None,
		enum: Sequence[Any] = None,
		format: str = None,
		description: str = None,
	):
		self.model = None
		self.name = None 
		self.type = type
		self.validator = va
		# TODO: if validator is None, use generic validator according to type
		self.callback = fn
		self.default = default
		self.required = False if default is None or default is not MISSING else True
		self.min = min
		self.max = max
		self.enum = enum
		self.format = format
		self.description = description
		return
	
	def __repr__(self):
		args = []
		if self.default:
			args.append('default={}'.format('\'{}\''.format(self.default) if isinstance(self.default, str) else repr(self.default)))
		if self.min:
			args.append('min={}'.format('\'{}\''.format(self.min) if isinstance(self.min, str) else repr(self.min)))
		if self.max:
			args.append('max={}'.format('\'{}\''.format(self.max) if isinstance(self.max, str) else repr(self.max)))
		if self.enum:
			args.append('enum={}'.format(self.enum))
		if self.validator:
			args.append('validator={}'.format(self.validator))
		if self.callback:
			args.append('callback={}'.format(self.callback))
		if self.description:
			args.append('description=\'{}\''.format(self.description))
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(args) if args else ''
		)

	def __set_name__(self, obj, name):
		if obj is None:
			return
		self.model = obj
		self.name = name
		return
	
	def __set__(self, obj, value, init: bool = False):
		if obj is None:
			return
		ex = self.name in obj.__properties__.keys()
		pv = obj.__properties__[self.name] if ex else None
		try:
			if value is None:
				if self.required:
					raise ValueError('{} is required in {}'.format(self.name, obj.__class__.__name__))
				obj.__properties__[self.name] = value
				return
			if self.validator:
				value = self.validator(value.__value__ if isinstance(value, Type) else value)
			obj.__properties__[self.name] = value
			if not init and self.callback:
				self.callback(
					obj,
					self,
					obj.__properties__[self.name],
					pv,
				)
			if not init and obj.__callback__:
				obj.__callback__(
					obj,
					self,
					obj.__properties__[self.name],
					pv,
				)
			return 
		except Exception as e:
			if ex:
				obj.__properties__[self.name] = pv
			raise e

	def __get__(self, obj, owner=None):
		if obj is None:
			return self
		if self.name not in obj.__properties__.keys():
			return self.default
		_ = obj.__properties__[self.name]
		return Type.Create(_, obj, self)
	
	def __delete__(self, obj):
		raise ValueError('{} is not able to delete in {}'.format(
			self.name,
			obj.__class__.__name__
		))
