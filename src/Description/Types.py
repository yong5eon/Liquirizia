# -*- coding: utf-8 -*-

from .Value import Descriptor, Type, Value, Condition, Schema
from typing import Optional, Union, Sequence, Any, Dict, Iterable 
from enum import Enum

__all__ = (
	'Boolean',
	'IntegerFormat',
	'Integer',
	'NumberFormat',
	'Number',
	'StringFormat',
	'String',
	'Binary',
	'BinaryBase64Encoded',
	'Array',
	'Object',
	'ObjectProperties',
)


class Boolean(Value):
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


class IntegerFormat(str, Enum):
	int32 = 'int32'
	int64 = 'int64'
	uint32 = 'uint32'
	uint64 = 'uint64'
	byte = 'byte'
	uuid = 'uuid'
	datetime = 'date-time'
	def __str__(self): return self.value


class Integer(Value):
	def __init__(
		self, 
		description: str = None,
		format: Union[str, IntegerFormat] = None,
		min: Any = None,
		max: Any = None,
		default: Any = None,
		enum: Optional[Sequence[str]] = None,
		required: bool = True,
	):
		super().__init__(
			type=Type.Integer,
			description=description,
			format=str(format) if format and isinstance(format, IntegerFormat) else format,
			min=min,
			max=max,
			default=default,
			enum=enum,
			required=required,
		)
		return


class NumberFormat(str, Enum):
	float = 'float'
	double = 'double'
	decimal = 'decimal'
	def __str__(self): return self.value


class Number(Value):
	def __init__(
		self, 
		description: str = None,
		format: Union[str, NumberFormat] = None,
		min: Any = None,
		max: Any = None,
		default: Any = None,
		enum: Optional[Sequence[str]] = None,
		required: bool = True,
	):
		super().__init__(
			type=Type.Number,
			description=description,
			format=str(format) if format and isinstance(format, NumberFormat) else format,
			min=min,
			max=max,
			default=default,
			enum=enum,
			required=required,
		)
		return


class StringFormat(str, Enum):
	datetime = 'date-time' # date-time, ISO 8601
	date = 'date' # date, ISO 8601
	time = 'time' # time, ISO 8601
	password = 'password' # password
	byte = 'byte' # byte, base64 encoded
	binary = 'binary' # binary
	email = 'email' # email
	uuid = 'uuid' # uuid
	uri = 'uri' # uri
	hostname = 'hostname' # hostname
	ipv4 = 'ipv4' # ipv4
	ipv6 = 'ipv6' # ipv6
	regex = 'regex' # regex
	xml = 'xml' # xml
	def __str__(self): return self.value


class String(Value):
	def __init__(
		self, 
		description: str = None,
		format: Union[str, StringFormat] = None,
		min: Any = None,
		max: Any = None,
		default: Any = None,
		enum: Optional[Sequence[str]] = None,
		required: bool = True,
	):
		super().__init__(
			type=Type.String,
			description=description,
			format=str(format) if format and isinstance(format, StringFormat) else format,
			min=min,
			max=max,
			default=default,
			enum=enum,
			required=required,
		)
		return


class BinaryBase64Encoded(String):
	def __init__(
		self, 
		description: str = None,
		default: str = None,
		required: bool = True,
	):
		super().__init__(
			description=description,
			format=StringFormat.byte,
			default=default,
			required=required,
		)
		return


class Binary(String):
	def __init__(
		self, 
		description: str = None,
		default: bytes = None,
		required: bool = True,
	):
		super().__init__(
			description=description,
			format=StringFormat.binary,
			default=default,
			required=required,
		)
		return


class Properties(Descriptor):
	def __init__(self, **kwargs: Dict[str, Union[Value, Condition, Schema]]):
		for k, v in kwargs.items():
			kwargs[k] = v.format if isinstance(v, Schema) else v
		super().__init__(**kwargs)
		return 
class Object(Descriptor):
	def __init__(
		self,
		description: Optional[str] = None,
		properties: Properties = Properties(),
		default: Dict = None,
		required: bool = True,
	):
		super().__init__(
			type=Type.Object,
			properties=properties,
		)
		if description: self['description'] = description
		self['required'] = []
		for k, v in properties.items():
			if hasattr(v, 'required') and getattr(v, 'required'):
				self['required'].append(k)
		if default: self['default'] = default
		self.required = required
		return


class Array(Descriptor):
	def __init__(
		self,
		description: str = None,
		format: Optional[Union[Value, Condition, Schema]] = None,
		default: Iterable = None,
		required: bool = True,
	):
		super().__init__(
			type=Type.Array,
		)
		if description: self['description'] = description
		if format: self['items'] = format.format if isinstance(format, Schema) else format
		if default: self['default'] = default
		self.required = required
		return
