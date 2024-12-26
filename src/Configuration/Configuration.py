# -*- coding: utf-8 -*-

from Liquirizia.Validator import Validator, Pattern
from Liquirizia.Validator.Patterns import *

from .Value import Value

from abc import ABCMeta, abstractmethod
from collections.abc import Mapping, Sequence
from copy import deepcopy
from ast import literal_eval
from os import environ

from typing import Type, ItemsView, KeysView, ValuesView, get_origin, get_args, Dict, List, Iterable, Union


__all__ = (
	'Configuration',
	'Handler',
)


class IsToTypeOf(Pattern):
	def __init__(self, t : Type, args : Iterable[Type] = None):
		self.type = t
		self.args = args
		return
	
	def __call__(self, parameter):
		try:
			if issubclass(self.type, str): return parameter
			# TODO : if self.type is subclass of List, do something
			return self.type(literal_eval(str(parameter)))
		except SyntaxError as e:
			raise TypeError('{}({}) is not type of {}'.format(parameter.__class__.__name__, parameter, self.type.__name__))
		except ValueError as e:
			raise ValueError('{} is not valid format to {}'.format(parameter, self.type.__name__))

	def __repr__(self):
		return '{}({})'.format(self.__class__.__name__, self.type.__name__)


class Creator(ABCMeta):
	"""Meta Class to create as Singleton"""
	def __call__(cls):
		try:
			o = getattr(cls, '__object__')
			return o
		except AttributeError:
			for k, t in cls.__annotations__.items():
				v = cls.__dict__[k] if k in cls.__dict__.keys() else None
				if isinstance(v, Value):
					continue
				ot = get_origin(t)
				otargs = get_args(t)
				if not ot:
					v = Value(
						k,
						default=v,
						va=Validator(IsToNone(IsToTypeOf(t)) if v is None else IsToTypeOf(t)),
					)
					v.__set_name__(cls, k)
					setattr(cls, k, v)
					continue
				if ot is Union:
					if type(None) not in otargs:
						raise TypeError('Union is not supported in {}'.format(cls.__name__))
					et = get_origin(otargs[0])
					etargs = get_args(otargs[0])
					if not et:
						v = Value(
							k,
							default=v,
							va=Validator(IsToNone(IsToTypeOf(otargs[0])) if v is None else IsToTypeOf(otargs[0])),
						)
						v.__set_name__(cls, k)
						setattr(cls, k, v)
						continue
					v = Value(
						k,
						default=v,
						va=Validator(IsToNone(IsToTypeOf(et, etargs)) if v is None else IsToTypeOf(et, etargs)),
					)
					v.__set_name__(cls, k)
					setattr(cls, k, v)
					continue
				v = Value(k, default=v, va=Validator(IsToTypeOf(ot, otargs)))
				v.__set_name__(cls, k)
				setattr(cls, k, v)
			o = super().__call__()
			if cls.__onLoad__: cls.__onLoad__(o)
			o.__env__()
			if cls.__onLoaded__: cls.__onLoaded__(o)
			cls.__object__ = o
			return o


class Configuration: pass
class Handler(metaclass=ABCMeta):
	@abstractmethod
	def __call__(self, conf: Configuration): pass

		
class Configuration(Mapping, metaclass=Creator):
	"""Abstract Configuration Class"""

	def __init__(self):
		self.__properties__ = {}
		return

	def __init_subclass__(
		cls, 
		onLoad: Handler = None,
		onLoaded: Handler = None,
	):
		cls.__onLoad__ = onLoad
		cls.__onLoaded__ = onLoaded
		return super().__init_subclass__()
	
	def __env__(self):
		for k, v in self.__class__.__dict__.items():
			if k not in self.__annotations__.keys(): continue
			if v.key in environ.keys():
				setattr(self, k, environ[v.key])
				continue
			if v.default is not None:
				setattr(self, k, v.default)
				continue
			setattr(self, k, None)
		return
	
	def __repr__(self):
		_ = []
		for k, v in self.__properties__.items():
			_.append('{}={}'.format(k, '\'{}\''.format(v) if isinstance(v, str) else v))
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(_),
		)

	# implements interface of Container
	def __contains__(self, key: object) -> bool:
		return self.__properties__.__contains__(key)
	
	# implements interface of Sized
	def __len__(self):
		return self.__properties__.__len__()

	# implements interfaces of Iterable 
	def __iter__(self):
		return self.__properties__.__iter__()

	# implements interfaces of Mapping
	def __getitem__(self, key):
		return self.__properties__.__getitem__(key)
	
	def keys(self) -> KeysView:
		return self.__properties__.keys()
	
	def items(self) -> ItemsView:
		return self.__properties__.items()
	
	def values(self) -> ValuesView:
		return self.__properties__.values()
	
	def __eq__(self, other: any) -> bool:
		return self.__properties__.__eq__(other)
	
	def __ne__(self, other: any) -> bool:
		return self.__properties__.__ne__(other)

	# copy
	def __copy__(self):
		return self.__class__.__new__(self.__class__, **self.__properties__)

	def __deepcopy__(self, memo={}):
		o = self.__class__.__new__(self.__class__, **self.__properties__)
		memo[id(self)] = o
		for k, v in self.__dict__.items():
			setattr(o, k, deepcopy(v, memo))
		return o
