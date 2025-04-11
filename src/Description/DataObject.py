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

from dataclasses import is_dataclass, MISSING, asdict
from json import dumps, loads
from typing import Type, Any, Union, Sequence, Iterable, Annotated, get_origin, get_args

__all__ = (
	'SchemaToDataObject',
	'DataObjectToSchema',
	'DataObjectToObject',
)


def SchemaToDataObject(o: Schema, name: str = None) -> object:
	# TODO : make dataclass according to schema dynamically
	raise NotImplementedError('SchemaToDataObject is not implemented yet')


class DataObjectToSchema(object):
	def __init__(self, mapper: TypeMapper = None):
		self.mapper = mapper
		return
	def __value__(
		self,
		o: type,
		format: Union[type, Sequence[type]] = None,
		description: str = None,
		required: bool = True,
		default: Any = MISSING,
		metadata: Any = None,
	) -> Union[Value, Schema]:
		args = get_args(o)
		o = get_origin(o) if get_origin(o) else o
		if args:
			if len(args) == 1:
				if o is list:
					return self.__value__(
						list,
						format=args[0],
						description=description,
						required=required,
						default=default,
						metadata=metadata,
					)
				if o is tuple:
					return self.__value__(
						tuple,
						format=args[0],
						description=description,
						required=required,
						default=default,
						metadata=metadata,
					)
				if o is set:
					return self.__value__(
						set,
						format=args[0],
						description=description,
						required=required,
						default=default,
						metadata=metadata,
					)
				if o is Union:
					return self.__value__(
						Union,
						format=args[0],
						description=description,
						required=required,
						default=default,
						metadata=metadata,
					)
				raise TypeError('{} is not a supported type'.format(o))
			if len(args) == 2:
				if o is Union:
					if args[0] is type(None): # Union[type, None]
						return self.__value__(
							args[1],
							description=description,
							required=False,
							default=None,
							metadata=metadata,
						)
					if args[1] is type(None): # Union[None, type]
						return self.__value__(
							args[0],
							description=description,
							required=False,
							default=None,
							metadata=metadata,
						)
					# Union[type, type]
					return self.__value__(
						o,
						format=(args[0], args[1]),
						description=description,
						required=required,
						default=default,
						metadata=metadata,
					)
				if o is dict: # Dict[type, type]
					return self.__value__(
						dict,
						description=description,
						required=required,
						default=default,
						metadata=metadata,
					)
				if o is Annotated:
					if isinstance(args[1], str):
						return self.__value__(
							args[0],
							description=args[1],
							required=required,
							default=default,
						)
					return self.__value__(
						args[0],
						description=description,
						required=required,
						default=default,
						metadata=args[1],
					)
				raise TypeError('{} is not a supported type'.format(o))	
			if o is Union:
				fs= [self.__value__(f) for f in args]
				return OneOf(*fs, required=required)
			if o is Annotated:
				if isinstance(args[1], str):
					return self.__value__(
						args[0],
						description=args[1],
						required=required,
						default=default,
						metadata=args[2] if isinstance(args[2], dict) else args[2:],
					)
				if isinstance(args[2], str):
					return self.__value__(
						args[0],
						description=args[2],
						required=required,
						default=default,
						metadata=args[1],
					)
				return self.__value__(
					args[0],
					description=description,
					required=required,
					default=default,
					metadata=args[1:],
				)
			raise TypeError('{} is not a supported type'.format(o))	
		if o is bool:
			kwargs = {
				'description': description,
				'required': required,
			}
			if default is not MISSING:
				kwargs['default'] = default
			if metadata and isinstance(metadata, dict):
				if 'description' in metadata.keys(): kwargs['description'] = metadata['description']
				if 'required' in metadata.keys(): kwargs['required'] = metadata['required']
			return Boolean(**kwargs)
		if o is int:
			kwargs = {
				'description': description,
				'required': required,
			}
			if default is not MISSING:
				kwargs['default'] = default
			if metadata and isinstance(metadata, dict):
				if 'description' in metadata.keys(): kwargs['description'] = metadata['description']
				if 'required' in metadata.keys(): kwargs['required'] = metadata['required']
				if 'format' in metadata.keys(): kwargs['format'] = metadata['format']
				if 'min' in metadata.keys(): kwargs['min'] = metadata['min']
				if 'max' in metadata.keys(): kwargs['max'] = metadata['max']
				if 'enum' in metadata.keys(): kwargs['enum'] = metadata['enum']
			return Integer(**kwargs)
		if o is float:
			kwargs = {
				'description': description,
				'required': required,
			}
			if default is not MISSING:
				kwargs['default'] = default
			if metadata and isinstance(metadata, dict):
				if 'description' in metadata.keys(): kwargs['description'] = metadata['description']
				if 'required' in metadata.keys(): kwargs['required'] = metadata['required']
				if 'format' in metadata.keys(): kwargs['format'] = metadata['format']
				if 'min' in metadata.keys(): kwargs['min'] = metadata['min']
				if 'max' in metadata.keys(): kwargs['max'] = metadata['max']
				if 'enum' in metadata.keys(): kwargs['enum'] = metadata['enum']
			return Number(**kwargs)
		if o is str:
			kwargs = {
				'description': description,
				'required': required,
			}
			if default is not MISSING:
				kwargs['default'] = default
			if metadata and isinstance(metadata, dict):
				if 'description' in metadata.keys(): kwargs['description'] = metadata['description']
				if 'required' in metadata.keys(): kwargs['required'] = metadata['required']
				if 'format' in metadata.keys(): kwargs['format'] = metadata['format']
				if 'min' in metadata.keys(): kwargs['min'] = metadata['min']
				if 'max' in metadata.keys(): kwargs['max'] = metadata['max']
				if 'enum' in metadata.keys(): kwargs['enum'] = metadata['enum']
			return String(**kwargs)
		if o is bytes:
			kwargs = {
				'description': description,
				'required': required,
			}
			if default is not MISSING:
				kwargs['default'] = default
			if metadata and isinstance(metadata, dict):
				if 'description' in metadata.keys(): kwargs['description'] = metadata['description']
				if 'required' in metadata.keys(): kwargs['required'] = metadata['required']
			return Binary(**kwargs)
		if o is list:
			kwargs = {
				'description': description,
				'required': required,
			}
			if default is not MISSING:
				kwargs['default'] = default
			if metadata and isinstance(metadata, dict):
				if 'description' in metadata.keys(): kwargs['description'] = metadata['description']
				if 'required' in metadata.keys(): kwargs['required'] = metadata['required']
				if 'format' in metadata.keys():
					if not isinstance(metadata['format'], Iterable):
						metadata['format'] = [metadata['format']]
					if len(metadata['format']) == 1:
						metadata['format'] = self.__value__(metadata['format'][0])
					fs = [self.__value__(f) for f in metadata['format']]
					kwargs['format'] = OneOf(*fs)
			if format:
				if not isinstance(format, Iterable):
					format = [format]
				if len(format) == 1:
					f = self.__value__(format[0])
					return Array(format=f, **kwargs)
				fs = [self.__value__(f) for f in format]
				return Array(format=OneOf(*fs), **kwargs)
			else:
				return Array(**kwargs)
		if o is tuple:
			kwargs = {
				'description': description,
				'required': required,
			}
			if default is not MISSING:
				kwargs['default'] = default
			if metadata and isinstance(metadata, dict):
				if 'description' in metadata.keys(): kwargs['description'] = metadata['description']
				if 'required' in metadata.keys(): kwargs['required'] = metadata['required']
			return Array(**kwargs)
		if o is set:
			kwargs = {
				'description': description,
				'required': required,
			}
			if default is not MISSING:
				kwargs['default'] = default
			if metadata and isinstance(metadata, dict):
				if 'description' in metadata.keys(): kwargs['description'] = metadata['description']
				if 'required' in metadata.keys(): kwargs['required'] = metadata['required']
			return Array(**kwargs)
		if o is dict:
			kwargs = {
				'description': description,
				'required': required,
			}
			if default is not MISSING:
				kwargs['default'] = default
			if metadata and isinstance(metadata, dict):
				if 'description' in metadata.keys(): kwargs['description'] = metadata['description']
				if 'required' in metadata.keys(): kwargs['required'] = metadata['required']
			return Object(**kwargs)
		if o is Union:
			kwargs = {}
			if default is not MISSING:
				kwargs['default'] = default
			if not format:
				raise TypeError('Union type must have format')
			if not isinstance(format, Iterable):
				format = [format]
			return OneOf(*[self.__value__(f) for f in format], **kwargs)
		if is_dataclass(o):
			return self.__call__(o, required=required)
		if self.mapper:
			V, kws = self.mapper(o)
			if V:
				if not issubclass(V, Value):
					raise TypeError('{} is not a Value'.format(V))
				kwargs = {
					'description': description,
					'required': required,
				}
				if default is not MISSING:
					kwargs['default'] = default
				if metadata and isinstance(metadata, dict):
					if 'description' in metadata.keys(): kwargs['description'] = metadata['description']
					if 'required' in metadata.keys(): kwargs['required'] = metadata['required']
					if V in (Integer, Number, String):
						if 'format' in metadata.keys(): kwargs['format'] = metadata['format']
						if 'min' in metadata.keys(): kwargs['min'] = metadata['min']
						if 'max' in metadata.keys(): kwargs['max'] = metadata['max']
						if 'enum' in metadata.keys(): kwargs['enum'] = metadata['enum']
				kwargs.update(kws)
				return V(**kwargs)
		raise TypeError('{} is not a supported type'.format(o))

	def __call__(self, o: Type[object], name: str = None, required: bool = True) -> Schema:
		if not is_dataclass(o):
			raise TypeError(f"'{o.__name__}' is not a DataObject(dataclass).")
		return Schema(
			name=name or o.__name__,
			format=Object(
				properties=Properties(
					**{
						f.name: self.__value__(
							f.type,
							required=True if f.default is MISSING and f.default_factory is MISSING else False,
							default=f.default,
						) for f in o.__dataclass_fields__.values()
					}
				),
				required=required,
			)
		)


class DataObjectToObject(object):
	def __init__(self, encoder: TypeEncoder = None):
		self.encoder = encoder
		return

	def __call__(self, o: object):
		if not is_dataclass(o):
			raise TypeError('{} is not a DataObject(dataclass).'.format(o.__class__.__name__))
		_ = dumps(
			asdict(o),
			default=self.encoder,
			ensure_ascii=False,
		)
		return loads(_)
