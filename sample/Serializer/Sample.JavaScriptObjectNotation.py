# -*- coding: utf-8 -*-

from Liquirizia.Serializer import SerializerHelper

from decimal import Decimal
from datetime import datetime, date, time

from collections.abc import MutableMapping, MutableSequence, MutableSet, Iterable
from typing import ItemsView, Iterator, KeysView, ValuesView, Any

class List(MutableSequence):
	def __init__(self, *args) -> None:
		self.__value__ : list = list(args)
		return
	def __repr__(self): return self.__value__.__repr__()
	def __iter__(self) -> Iterator:
		return self.__value__.__iter__()
	def __reversed__(self) -> Iterator:
		return self.__value__.__reversed__()
	def __contains__(self, value: Any) -> bool:
		return self.__value__.__contains__(value)
	def __len__(self) -> int:
		return self.__value__.__len__()
	def __getitem__(self, index: int) -> Any:
		return self.__value__.__getitem__(index)
	def __setitem__(self, index: int, value: Any) -> None:
		return self.__value__.__setitem__(index, value)
	def __delitem__(self, index: int) -> None:
		return self.__value__.__delitem__(index)
	def __iadd__(self, values: Iterable):
		return self.__value__.__iadd__(values)
	def insert(self, index: int, value: Any) -> None:
		return self.__value__.insert(index, value)
	def append(self, value: Any) -> None:
		return self.__value__.append(value)
	def clear(self) -> None:
		return self.__value__.clear()
	def extend(self, values: Iterable) -> None:
		return self.__value__.extend(values)
	def pop(self, index: int = -1) -> Any:
		return self.__value__.pop(index)
	def remove(self, value: Any) -> None:
		return self.__value__.remove(value)
	def reverse(self) -> None:
		return self.__value__.reverse()

class Dictionary(MutableMapping):
	def __init__(self, **kwargs):
		self.__value__ : dict = dict(kwargs)
		return
	def __repr__(self): return self.__value__.__repr__()
	def __getitem__(self, key: Any) -> Any:
		return self.__value__.__getitem__(key)
	
	def __setitem__(self, key: Any, value: Any) -> None:
		return self.__value__.__setitem__(key, value)
	
	def __delitem__(self, key: Any) -> None:
		return self.__value__.__delitem__(key)
	
	def __iter__(self) -> Iterator:
		return self.__value__.__iter__()
	
	def __len__(self) -> int:
		return self.__value__.__len__()
	
	def __contains__(self, key: object) -> bool:
		return self.__value__.__contains__(key)
	
	def keys(self) -> KeysView:
		return self.__value__.keys()
	
	def items(self) -> ItemsView:
		return self.__value__.items()
	
	def values(self) -> ValuesView:
		return self.__value__.values()
	
	def __eq__(self, other: object) -> bool:
		return self.__value__.__eq__(other)
	
	def __ne__(self, value: object) -> bool:
		return self.__value__.__ne__(value)
	
	def get(self, key: object) -> Any:
		return self.__value__.get(key)

class Set(MutableSet):
	def __init__(self, *args):
		self.__value__ : set = set(args)
	def __repr__(self): return self.__value__.__repr__()
	def __contains__(self, x):
		return self.__value__.__contains__(x)
	def __iter__(self):
		return self.__value__.__iter__()
	def __len__(self):
		return self.__value__.__len__()
	def __ior__(self, it):
		return self.__value__.__ior__(it)
	def __iand__(self, it):
		return self.__value__.__iand__(it)
	def __ixor__(self, it):
		return self.__value__.__ixor__(it)
	def __isub__(self, it):
		return self.__value__.__isub__(it)
	def __le__(self, other):
		return self.__value__.__le__(other)
	def __lt__(self, other):
		return self.__value__.__lt__(other)
	def __eq__(self, other):
		return self.__value__.__eq__(other)
	def __ne__(self, value):
		return self.__value__.__ne__(value)
	def __gt__(self, other):
		return self.__value__.__gt__(other)
	def __ge__(self, other):
		return self.__value__.__ge__(other)
	def __and__(self, other):
		return self.__value__.__and__(other)
	def __or__(self, other):
		return self.__value__.__or__(other)
	def __sub__(self, other):
		return self.__value__.__sub__(other)
	def __xor__(self, other):
		return self.__value__.__xor__(other)
	def add(self, value):
		return self.__value__.add(value)
	def discard(self, value):
		return self.__value__.discard(value)
	def clear(self):
		return self.__value__.clear()
	def pop(self):
		return self.__value__.pop()
	def remove(self, value):
		return self.__value__.remove(value)
	def isdisjoint(self, other):
		return self.__value__.isdisjoint(other)



if __name__ == '__main__':


	encoded = SerializerHelper.Encode(True, format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode(0, format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode(0.0, format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode(Decimal('0.0'), format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode('String', format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode(datetime.now(), format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode(datetime.now().date(), format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode(datetime.now().time(), format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode([1,2,3], format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode((4,5,6), format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	_ = {
		'a': True,
		'b': 0,
		'c': 0.0,
		'd': 'String',
		'e': [1,2,3],
		'f': (1,2,3),
		'g': {
			'a': True,
			'b': 0,
			'c': 0.0,
			'd': 'String',
			'e': [1,2,3],
			'f': (1,2,3),
			'g': {}
		}
	}
	encoded = SerializerHelper.Encode(_, format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	_ = List(1,2,3,3)
	encoded = SerializerHelper.Encode(_, format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	_ = Set(1,2,3,3)
	encoded = SerializerHelper.Encode(_, format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	_ = Dictionary(
		a=True,
		b=1,
		c=1.0,
		d='string',
		e=[1,2,3,3],
		f=(1,2,3,3),
		g={1,2,3,3},
		h={
			'a': False,
			'b': 2,
			'c': 2.0,
			'd': 'characters',
			'e': [1,2,3,3],
			'f': (1,2,3,3),
			'g': {1,2,3,3},
		}
	)
	encoded = SerializerHelper.Encode(_, format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

