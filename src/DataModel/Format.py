# -*- coding: utf-8 -*-

from collections.abc import Mapping

from enum import  Enum

from typing import Any, Iterator, KeysView, ItemsView, ValuesView
from typing import Optional, Union, Sequence

__all__ = (
	'Type',
	'Boolean',
	'Integer',
	'Number',
	'String',
	'Array',
	'Object',
	'ObjectProperties',
	'OneOf',
)


class Descriptor(Mapping):
	def __init__(self, **kwargs):
		self.__properties__ = kwargs
		return
	
	def __repr__(self): return self.__properties__.__repr__()

	def __getitem__(self, key: Any) -> Any:
		return self.__properties__.__getitem__(key)
	
	def __setitem__(self, key: Any, value: Any) -> None:
		return self.__properties__.__setitem__(key, value)
	
	def __delitem__(self, key: Any) -> None:
		return self.__properties__.__delitem__(key)
	
	def __iter__(self) -> Iterator:
		return self.__properties__.__iter__()
	
	def __len__(self) -> int:
		return self.__properties__.__len__()
	
	def __contains__(self, key: object) -> bool:
		return self.__properties__.__contains__(key)
	
	def keys(self) -> KeysView:
		return self.__properties__.keys()
	
	def items(self) -> ItemsView:
		return self.__properties__.items()
	
	def values(self) -> ValuesView:
		return self.__properties__.values()
	
	def __eq__(self, other: object) -> bool:
		return self.__properties__.__eq__(other)
	
	def __ne__(self, value: object) -> bool:
		return self.__properties__.__ne__(value)
	
	def get(self, key: object) -> Any:
		return self.__properties__.get(key)

class Type(str, Enum):
	Boolean = 'boolean'
	Integer = 'integer'
	Number = 'number'
	String = 'string'
	Array = 'array'
	Object = 'object'

	def __repr__(self): return '\'{}\''.format(self.value)


class Boolean(Descriptor):
	def __init__(
		self, 
		description: str = None,
		default: Any = None,
		required: bool = True,

	):
		super().__init__(
			type=Type.Boolean,
			description=description,
			default=default,
			required=required,
		)
		return

class Integer(Descriptor):
	def __init__(
		self, 
		description: str = None,
		format: str = None,
		min: int = None,
		max: int = None,
		default: int = None,
		ins: Optional[Sequence[int]] = None,
		required: bool = True,
	):
		super().__init__(
			type=Type.Integer,
			required=required,
		)
		if description: self['description'] = description
		if format: self['format'] = format
		if min: self['minimum'] = min
		if max: self['maximum'] = max
		if default: self['default'] = default
		if ins: self['enum'] = ins
		return


class Number(Descriptor):
	def __init__(
		self, 
		description: str = None,
		format: str = None,
		min: float = None,
		max: float = None,
		default: float = None,
		ins: Optional[Sequence[float]] = None,
		required: bool = True,
	):
		super().__init__(
			type=Type.Number,
			required=required,
		)
		if description: self['description'] = description
		if format: self['format'] = format
		if min: self['minimum'] = min
		if max: self['maximum'] = max
		if default: self['default'] = default
		if ins: self['enum'] = ins
		return


class String(Descriptor):
	def __init__(
		self, 
		description: str = None,
		format: str = None,
		default: str = None,
		ins: Optional[Sequence[str]] = None,
		required: bool = True,
	):
		super().__init__(
			type=Type.String,
			required=required,
		)
		if description: self['description'] = description
		if format: self['format'] = format
		if default: self['default'] = default
		if ins: self['enum'] = ins
		return


class ObjectProperties(Descriptor): pass
class Object(Descriptor):
	def __init__(
		self,
		properties: ObjectProperties,
		description: Optional[str] = None,
		requires: Optional[Sequence[str]] = None,
	):
		super().__init__(
			type=Type.Object,
			properties=properties,
		)
		if description: self['description'] = description
		if requires: self['required'] = requires
		return


class Array(Descriptor): pass
class Array(Descriptor):
	def __init__(
		self,
		format: Optional[Union[Boolean, Integer, Number, String, Array, Object]] = None,
		description: str = None,
		required: bool = True,
	):
		super().__init__(
			type=Type.Array,
			required=required,
		)
		if format: self['items'] = format
		if description: self['description'] = description
		return


class OneOf(Descriptor):
	def __init__(self, *args):
		super().__init__(oneOf=args)
		return
