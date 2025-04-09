# -*- coding: utf-8 -*-

from .Value import (
	Value,
	Schema,
	OneOf,
	AllOf,
)

from .Types import (
	Boolean,
	IntegerFormat,
	Integer,
	NumberFormat,
	Number,
	StringFormat,
	String,
	Binary,
	BinaryBase64Encoded,
	Array,
	Object,
	Properties,
)

__all__ = (
	'Value',
	'Schema',
	'OneOf',
	'AllOf',
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
	'Properties',
	'ToSchema',
)

from dataclasses import is_dataclass
from ..DataModel import Model
from typing import Type, Union, get_origin, get_args


def ToSchema(o: Union[Type[object], Type[Model]], name: str = None) -> Schema:
	if is_dataclass(o):
		return DataObjectToSchema(o, name)
	elif issubclass(o, Model):
		return DataModelToSchema(o, name)
	return None


def TypeToValue(o: type, description: str = None, required: bool = True) -> Union[Value, Schema]:
	args = get_args(o)
	o = get_origin(o) if get_origin(o) else o
	if args:
		if len(args) == 1:
			return TypeToValue(args[0], description, required)
		elif len(args) == 2:
			if o is Union:
				if args[0] is type(None):
					return TypeToValue(args[1], description, required=False)
				elif args[1] is type(None):
					return TypeToValue(args[0], description, required=False)
				else:
					raise TypeError('Union must be NoneType or a single type')
			else:
				raise TypeError('{} is not a supported type'.format(o))	
		else:
			raise TypeError('{} is not a supported type'.format(o))	
	if o is bool:
		return Boolean(description=description, required=required)
	elif o is int:
		return Integer(description=description, required=required)
	elif o is float:
		return Number(description=description, required=required)
	elif o is str:
		return String(description=description, required=required)
	elif o is bytes:
		return Binary(description=description, required=required)
	elif o is list:
		return Array(description=description, required=required)
	elif o is dict:
		return Object(description=description, required=required)
	else:
		if is_dataclass(o):
			return DataObjectToSchema(o, description, required=required)
		elif issubclass(o, Model):
			return DataModelToSchema(o, description, required=required)
		raise TypeError('{} is not a supported type'.format(o))


def DataObjectToSchema(o: Type[object], name: str = None, required: bool = True) -> Schema:
	if not is_dataclass(o):
		raise TypeError(f"'{o.__name__}' is not a DataObject(dataclass).")
	return Schema(
		name=name or o.__name__,
		format=Object(
			properties=Properties(
				**{f.name: TypeToValue(f.type, required=False if f.default is None else True) for f in o.__dataclass_fields__.values()}
			),
			required=required,
		)
	)


def DataModelToSchema(o: Type[Model], name: str = None, required: bool = True) -> Schema:
	if not issubclass(o, Model):
		raise TypeError(f"'{o.__name__}' is not a DataModel.")
	return Schema(
		name=name or o.__name__,
		format=Object(
			properties=Properties(
				# TODO : Add support for Model fields
				# **{f.name: Value.to_schema(f.type) for f in o.__dataclass_fields__.values()}
			),
			required=required,
		)
	)