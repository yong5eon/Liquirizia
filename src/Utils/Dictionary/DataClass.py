# -*- coding: utf-8 -*-

from dataclasses import make_dataclass, fields, is_dataclass
from typing import Any, Dict, Type

__all__ = (
	'ToDataClass',
	'CreateDataClass',
)


def ToDataClass(data: Dict[str, Any], cls: Type[Any]) -> Any:
	if not is_dataclass(cls):
		raise TypeError('{} is not a dataclass'.format(cls.__name__))
	
	field_names = {f.name for f in fields(cls)}
	filtered_data = {k: v for k, v in data.items() if k in field_names}
	return cls(**filtered_data)

def CreateDataClass(name: str, data: Dict[str, Any]) -> Type[Any]:
	fields = [(key, type(value)) for key, value in data.items()]
	return make_dataclass(name, fields)
