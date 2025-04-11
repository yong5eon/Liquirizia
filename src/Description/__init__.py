# -*- coding: utf-8 -*-

from .Value import (
	Value,
	Condition,
	Schema,
	OneOf,
	AllOf,
	TypeMapper,
	TypeEncoder,
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
from .DataObject import (
	DataObjectToSchema,
	DataObjectToObject,
)

from dataclasses import is_dataclass
from typing import Type, Dict
from collections.abc import Sequence, Mapping
from json import dumps, loads, JSONEncoder

__all__ = (
	# Value
	'Value',
	'Schema',
	'OneOf',
	'AllOf',
	'TypeMapper',
	'TypeEncoder',
	# Types
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
	# Utils
	'ToSchema',
	'DumpSchema',
	# 'SchemaToDataObject',
	'ToObject',
)


class SchemaEncoder(JSONEncoder):
	"""Type Encoder for JSON"""
	def default(self, obj):
		if isinstance(obj, Sequence):
			return list(obj)
		if isinstance(obj, Mapping):
			return dict(obj)
		if isinstance(obj, Schema):
			return obj.format
		if isinstance(obj, Condition):
			_ = []
			for arg in obj.args:
				if isinstance(arg, Schema):
					_.append(arg.format)
					continue
				if isinstance(arg, Value):
					_.append(arg)
					continue
				raise TypeError('{} is not supported'.format(arg.__class__.__name__))
			return {'oneOf': _}
		return None


def DumpSchema(o: Schema):
	def encode(schema: Schema):
		return dumps(
			schema,
			cls=SchemaEncoder,
			ensure_ascii=False,
		)
	if not isinstance(o, Schema):
		raise TypeError('{} is not a Schema'.format(o.__name__))
	return loads(encode(o))


def SchemaToDataObject(o: Schema, name: str = None) -> object:
	# TODO : make dataclass according to schema dynamically
	raise NotImplementedError('SchemaToDataObject is not implemented yet')


def ToSchema(o: Type[object], name: str = None, typedef: TypeMapper = None) -> Schema:
	dataObjectToSchema = DataObjectToSchema(mapper=typedef)
	if is_dataclass(o):
		return dataObjectToSchema(o, name)
	raise ValueError('{} cannot be converted to Schema'.format(o.__name__))


def ToObject(o: object, typeenc: TypeEncoder = None) -> Dict:
	# TODO : make dict object according to schema dynamically
	dataObjectToObject = DataObjectToObject(encoder=typeenc)
	if is_dataclass(o):
		return dataObjectToObject(o)
	raise ValueError('{} cannot be converted to Object'.format(o.__name__))
