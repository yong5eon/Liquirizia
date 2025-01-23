# -*- coding: utf-8 -*-

from ..Model import Model
from ..Format import Object, ObjectProperties

from copy import copy
from json import dumps

from typing import Dict, Mapping, Type

__all__ = (
	'ToDict',
	'ToSchema',
	'SchemaToJSON',
)


def ToDict(o: Model) -> Dict:
	return copy(o.__properties__)


def ToSchema(o: Type[Model]) -> Dict:
	if o.__schema__: return o.__schema__
	ops = ObjectProperties()
	requires = []
	for k, v in o.__mapper__.items():
		requires.append(k)
		ops[k] = v.format
	return Object(
		properties=ops,
		description=o.__description__,
		requires=requires
	)


def encoder(o: any):
	if(isinstance(o, Mapping)): return dict(o)
	raise TypeError('{} is not JSON encode'.format(type(o)))


def SchemaToJSON(o: Object, indent: int = 2):
	return dumps(o, ensure_ascii=False, indent=indent, default=encoder)
