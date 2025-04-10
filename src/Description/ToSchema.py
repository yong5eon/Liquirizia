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

from dataclasses import is_dataclass, MISSING
from ..DataModel import Model
from typing import Type, Union, Sequence, Mapping, Iterable, get_origin, get_args
from sys import stdout
from json import dumps, loads, JSONEncoder

__all__ = (
	'ToSchema',
	'DumpSchema',
	'SchemaToDataObject',
	'SchemaToDataModel',
)


class TypeEncoder(JSONEncoder):
	"""Type Encoder for JSON"""
	def default(self, obj):
		if isinstance(obj, Sequence):
			return tuple(obj)
		if isinstance(obj, Mapping):
			return dict(obj)
		return None


def DumpSchema(o: Schema):
	def encode(schema: Schema):
		return dumps(
			schema,
			cls=TypeEncoder,
			ensure_ascii=False,
		)
	if not isinstance(o, Schema):
		raise TypeError('{} is not a Schema'.format(o.__name__))
	return loads(encode(o.format))


def SchemaToDataObject(o: Schema, name: str = None) -> object:
	# TODO : make dataclass according to schema dynamically
	raise NotImplementedError('SchemaToDataObject is not implemented yet')

def SchemaToDataModel(o: Schema, name: str = None) -> Model:
	# TODO : make DataModel according to schema dynamically
	raise NotImplementedError('SchemaToDataModel is not implemented yet')


def ToSchema(o: Union[Type[object], Type[Model]], name: str = None) -> Schema:
	ObjectToSchema = DataObjectToSchema()
	ModelToSchema = DataModelToSchema()
	if is_dataclass(o):
		return ObjectToSchema(o, name)
	elif issubclass(o, Model):
		return ModelToSchema(o, name)
	return None


class DataObjectToSchema(object):
	def __value__(self, o: type, format: Union[type, Sequence[type]] = None, description: str = None, required: bool = True) -> Union[Value, Schema]:
		args = get_args(o)
		o = get_origin(o) if get_origin(o) else o
		if args:
			if len(args) == 1:
				if o is list:
					return self.__value__(list, args[0], description, required)
				elif o is tuple:
					return self.__value__(tuple, args[0], description, required)
				elif o is set:
					return self.__value__(set, args[0], description, required)
				else:
					raise TypeError('{} is not a supported type'.format(o))
			elif len(args) == 2:
				# Union[type, None]
				# Union[None, type]
				# Union[type, type]
				# Dict[type, type]
				if o is Union:
					if args[0] is type(None):
						return self.__value__(args[1], description=description, required=False)
					elif args[1] is type(None):
						return self.__value__(args[0], description=description, required=False)
					else:
						return self.__value__(o, format=(args[0], args[1]), description=description, required=required)
				else:
					if o is dict:
						return self.__value__(dict, description=description, required=required)
					else:
						raise TypeError('{} is not a supported type'.format(o))	
			else:
				if o is Union:
					fs= [self.__value__(f) for f in args]
					# return OneOf(*fs, description=description, required=required)
					raise TypeError('multi-formatted is not a supported type')
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
			if format:
				if not isinstance(format, Iterable):
					format = [format]
				if len(format) == 1:
					f= self.__value__(format[0])
					return Array(format=f, description=description, required=required)
				else:
					fs= [self.__value__(f) for f in format]
					# return Array(format=OneOf(*fs), description=description, required=required)
					raise TypeError('multi-formatted {} is not a supported type'.format(o))
			else:
				return Array(description=description, required=required)
		elif o is tuple:
			return Array(description=description, required=required)
		elif o is set:
			return Array(description=description, required=required)
		elif o is dict:
			return Object(description=description, required=required)
		else:
			if is_dataclass(o):
				return self.__call__(o, required=required)
			# TODO : support DataModel
			# elif issubclass(o, Model):
			# 	return self.__model__(o, description=description, required=required)
			raise TypeError('{} is not a supported type'.format(o))
	
	
	def __call__(self, o: Type[object], name: str = None, required: bool = True) -> Schema:
		if not is_dataclass(o):
			raise TypeError(f"'{o.__name__}' is not a DataObject(dataclass).")
		return Schema(
			name=name or o.__name__,
			format=Object(
				properties=Properties(
					**{f.name: self.__value__(f.type, required=True if f.default is MISSING and f.default_factory is MISSING else False) for f in o.__dataclass_fields__.values()}
				),
				required=required,
			)
		)


class DataModelToSchema(object):
	def __call__(self, o: Type[Model], name: str = None, required: bool = True) -> Schema:
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
