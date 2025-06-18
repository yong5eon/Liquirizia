# -*- coding: utf-8 -*-

from .Value import (
	Value,
	Schema,
	OneOf,
	TypeMapper,
	TypeEncoder,
)

from .Types import (
	Boolean,
	Integer,
	Number,
	String,
	Binary,
	Array,
	Object,
	Properties,
)

from ..DataModel import Model, MISSING
from json import dumps, loads
from typing import (
	Type,
	Any,
	Union,
	Sequence,
	Iterable,
	Annotated,
	get_origin,
	get_args,
	ForwardRef,
)

__all__ = (
	'SchemaToDataModel',
	'DataModelToSchema',
	'DataModelToObject',
)


def SchemaToDataModel(o: Schema, name: str = None) -> object:
	# TODO : make Model according to schema dynamically
	raise NotImplementedError('SchemaToDataObject is not implemented yet')


class DataModelToSchema(object):
	def __init__(self):
		return
	def __value__(
		self,
		o: type,
		format: Union[type, Sequence[type]] = None,
		description: str = None,
		required: bool = True,
		default: Any = MISSING,
		min: Any = None,
		max: Any = None,
		enum: Sequence[Any] = None,
	) -> Union[Value, Schema]:
		kwargs = {
			'required': required,
		}
		if format: kwargs['format'] = format
		if description: kwargs['description'] = description
		if default is not MISSING: kwargs['default'] = default
		if min is not None: kwargs['min'] = min
		if max is not None: kwargs['max'] = max
		if enum is not None: kwargs['enum'] = enum
		if o is bool:
			return Boolean(**kwargs)
		if o is int:
			return Integer(**kwargs)
		if o is float:
			return Number(**kwargs)
		if o is str:
			return String(**kwargs)
		if o is bytes:
			return Binary(**kwargs)
		if o in (list, tuple, set):
			# TODO : format 
			return Array(**kwargs)
		if o is dict:
			return Object(**kwargs)
		raise TypeError('{} is not a supported type'.format(o))

	def __call__(self, o: Type[Model], description:str = None, required: bool = True) -> Schema:
		if not issubclass(o, Model):
			raise TypeError('{} is not a DataModel.'.format(o.__model__))
		kwargs = {}
		for k, v in o.__mapper__.items():
			kwargs[k] = self.__value__(
				v.type,
				format=v.format,
				description=v.description,
				required=v.required,
				default=v.default,
				min=v.min,
				max=v.max,
				enum=v.enum,
			)
		return Schema(
			name=description or o.__model__,
			format=Object(
				description=description or o.__model__,
				properties=Properties(**kwargs),
				required=required,
			)
		)


class DataModelToObject(object):
	def __init__(self, encoder: TypeEncoder = None):
		self.encoder = encoder
		return

	def __call__(self, o: Model):
		if not isinstance(o, Model):
			raise TypeError('{} is not a DataModel.'.format(o.__class__.__name__))
		_ = dumps(
			o,
			default=self.encoder,
			ensure_ascii=False,
		)
		return loads(_)
