# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Serializer import SerializerHelper, Serializer

from collections.abc import MutableMapping, MutableSequence, MutableSet, Iterable, Sequence, Mapping
from typing import ItemsView, Iterator, KeysView, ValuesView, Any

from decimal import Decimal
from datetime import datetime, date, time

cdt  = datetime.now()
cd = cdt.date()
ct = cdt.time()


class List(MutableSequence):
	def __init__(self, *args) -> None:
		self.__value__ : list = list(args)
		return
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


class SampleEncoder(Serializer):
	def __call__(self, obj):
		return str(obj)
	

class SampleDecoder(Serializer):
	def __call__(self, obj):
		return int(obj)


class TestSerializer(Case):
	@classmethod
	def setUpClass(cls) -> None:
		SerializerHelper.Set('int', SampleEncoder, SampleDecoder)
		return super().setUpClass()

	@classmethod
	def tearDownClass(cls) -> None:
		return super().tearDownClass()

	@Order(0)
	def testGetSupportFormats(self):
		ASSERT_TRUE('int' in SerializerHelper.GetSupportFormats())
		return

	@Parameterized(
		{'v': 0, 'serialized': '0'},
		{'v': 1, 'serialized': '1'},
	)
	@Order(1)
	def testSerialize(self, v, serialized):
		ASSERT_TRUE(SerializerHelper.Serialize(v, format='int') == serialized)
		return

	@Parameterized(
		{'v': '0', 'deserialized': 0},
		{'v': '1', 'deserialized': 1},
	)
	@Order(2)
	def testDesrialize(self, v, deserialized):
		ASSERT_TRUE(SerializerHelper.Deserialize(v, format='int') == deserialized) 
		return

	@Parameterized(
		{'v': '0', 'pack': b'0'},
		{'v': '1', 'pack': b'1'},
	)
	@Order(3)
	def testPack(self, v, pack):
		ASSERT_TRUE(SerializerHelper.Pack(v, charset='utf-8') == pack)
		return

	@Parameterized(
		{'v': b'0', 'unpack': '0'},
		{'v': b'1', 'unpack': '1'},
	)
	@Order(4)
	def testUnpack(self, v, unpack):
		ASSERT_TRUE(SerializerHelper.Unpack(v, charset='utf-8') == unpack)
		return

	@Parameterized(
		{'v': 0, 'encoded': b'0'},
		{'v': 1, 'encoded': b'1'},
	)
	@Order(5)
	def testEncode(self, v, encoded):
		ASSERT_IS_EQUAL(SerializerHelper.Encode(v, format='int', charset='utf-8'), encoded)
		return

	@Parameterized(
		{'v': b'0', 'decoded': 0},
		{'v': b'1', 'decoded': 1},
	)
	@Order(6)
	def testDecode(self, v, decoded):
		ASSERT_TRUE(SerializerHelper.Decode(v, format='int', charset='utf-8') == decoded) 
		return

	@Parameterized(
		{'v': True, 'exp': b'True'},
		{'v': False, 'exp': b'False'},
		{'v': 1, 'exp': b'1'},
		{'v': 1.0, 'exp': b'1.0'},
		{'v': Decimal('1.0'), 'exp': b'1.0'},
		{'v': 'string', 'exp': b'string'},
		{'v': [1,2,3,3], 'exp': b'[1, 2, 3, 3]'},
		{'v': (1,2,3,3), 'exp': b'(1, 2, 3, 3)'},
		{'v': {1,2,3,3}, 'exp': b'{1, 2, 3}'},
		{'v': {
			'a': True,
			'b': 0,
			'c': 0.0,
			'd': 'String',
			'e': [1,2,3],
			'f': (1,2,3),
			'g': {1,2,2},
			'h': {
				'a': True,
				'b': 0,
				'c': 0.0,
				'd': 'String',
				'e': [1,2,3],
				'f': (1,2,3),
				'g': {2,3,3}
			}
		}, 'exp': b"{'a': True, 'b': 0, 'c': 0.0, 'd': 'String', 'e': [1, 2, 3], 'f': (1, 2, 3), 'g': {1, 2}, 'h': {'a': True, 'b': 0, 'c': 0.0, 'd': 'String', 'e': [1, 2, 3], 'f': (1, 2, 3), 'g': {2, 3}}}"},
		# {'v': cdt, 'exp': cdt.isoformat().encode()},
		# {'v': cd, 'exp': cd.isoformat().encode()},
		# {'v': ct, 'exp': cd.isoformat().encode()},
	)
	@Order(7)
	def testText(self, v, exp):
		encoded = SerializerHelper.Encode(v, format='text', charset='utf-8')
		decoded = SerializerHelper.Decode(encoded, format='text', charset='utf-8')
		ASSERT_IS_EQUAL(encoded, exp)
		ASSERT_IS_EQUAL(decoded, v)
		return

	@Parameterized(
		{'v': List(1,2,3,3), 'exp': b'[1, 2, 3, 3]'},
	)
	@Order(8)
	def testTextSequeuce(self, v, exp):
		encoded = SerializerHelper.Encode(v, format='text', charset='utf-8')
		decoded = SerializerHelper.Decode(encoded, format='text', charset='utf-8')
		ASSERT_IS_EQUAL(encoded, exp)
		ASSERT_IS_EQUAL_SEQUENCE(decoded, v)
		return

	@Parameterized(
		{'v': Set(1,2,3,3), 'exp': b'{1, 2, 3}'},
	)
	@Order(9)
	def testTextSet(self, v, exp):
		encoded = SerializerHelper.Encode(v, format='text', charset='utf-8')
		decoded = SerializerHelper.Decode(encoded, format='text', charset='utf-8')
		ASSERT_IS_EQUAL(encoded, exp)
		ASSERT_IS_EQUAL_SEQUENCE(decoded, v)
		return

	@Parameterized(
		{'v': Dictionary(
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
		), 'exp': b"{'a': True, 'b': 1, 'c': 1.0, 'd': 'string', 'e': [1, 2, 3, 3], 'f': (1, 2, 3, 3), 'g': {1, 2, 3}, 'h': {'a': False, 'b': 2, 'c': 2.0, 'd': 'characters', 'e': [1, 2, 3, 3], 'f': (1, 2, 3, 3), 'g': {1, 2, 3}}}"},
	)
	@Order(10)
	def testTextDictionary(self, v, exp):
		encoded = SerializerHelper.Encode(v, format='text', charset='utf-8')
		decoded = SerializerHelper.Decode(encoded, format='text', charset='utf-8')
		ASSERT_IS_EQUAL(encoded, exp)
		ASSERT_IS_EQUAL_DICT(decoded, v.__value__)
		return


	@Parameterized(
		{'v': True, 'exp': b'true'},
		{'v': False, 'exp': b'false'},
		{'v': 1, 'exp': b'1'},
		{'v': 1.0, 'exp': b'1.0'},
		{'v': Decimal('1.0'), 'exp': b'1.0'},
		{'v': 'string', 'exp': b'"string"'},
		{'v': [1,2,3,3], 'exp': b'[1, 2, 3, 3]'},
		{'v': (1,2,3,3), 'exp': b'[1, 2, 3, 3]'},
		{'v': {1,2,3,3}, 'exp': b'[1, 2, 3]'},
		{'v': {
			'a': True,
			'b': 0,
			'c': 0.0,
			'd': 'String',
			'e': [1,2,3],
			'f': (1,2,3),
			'g': {1,2,2},
			'h': {
				'a': True,
				'b': 0,
				'c': 0.0,
				'd': 'String',
				'e': [1,2,3],
				'f': (1,2,3),
				'g': {2,3,3}
			}
		}, 'exp': b'{"a": true, "b": 0, "c": 0.0, "d": "String", "e": [1, 2, 3], "f": [1, 2, 3], "g": [1, 2], "h": {"a": true, "b": 0, "c": 0.0, "d": "String", "e": [1, 2, 3], "f": [1, 2, 3], "g": [2, 3]}}'},
		{'v': cdt, 'exp': '"{}"'.format(cdt.isoformat()).encode()},
		{'v': cd, 'exp': '"{}"'.format(cd.isoformat()).encode()},
		{'v': ct, 'exp': '"{}"'.format(ct.isoformat()).encode()},
		{'v': '01000000000', 'exp': b'"01000000000"'},
		{'v': '01011111111', 'exp': b'"01011111111"'},
		{'v': ['01011111111'], 'exp': b'["01011111111"]'},
		{'v': {'a':'01011111111'}, 'exp': b'{"a": "01011111111"}'},
		{'v': [{'a':'01011111111'}], 'exp': b'[{"a": "01011111111"}]'},
	)
	@Order(11)
	def testJSON(self, v, exp):
		encoded = SerializerHelper.Encode(v, format='json', charset='utf-8')
		decoded = SerializerHelper.Decode(encoded, format='json', charset='utf-8')
		ASSERT_IS_EQUAL(encoded, exp)
		return

	@Parameterized(
		{'v': List(1,2,3,3), 'exp': b'[1, 2, 3, 3]'},
	)
	@Order(12)
	def testJSONSequeuce(self, v, exp):
		encoded = SerializerHelper.Encode(v, format='json', charset='utf-8')
		decoded = SerializerHelper.Decode(encoded, format='json', charset='utf-8')
		ASSERT_IS_EQUAL(encoded, exp)
		return

	@Parameterized(
		{'v': Set(1,2,3,3), 'exp': b'[1, 2, 3]'},
	)
	@Order(13)
	def testJSONSet(self, v, exp):
		encoded = SerializerHelper.Encode(v, format='json', charset='utf-8')
		decoded = SerializerHelper.Decode(encoded, format='json', charset='utf-8')
		ASSERT_IS_EQUAL(encoded, exp)
		return

	@Parameterized(
		{'v': Dictionary(
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
		), 'exp': b'{"a": true, "b": 1, "c": 1.0, "d": "string", "e": [1, 2, 3, 3], "f": [1, 2, 3, 3], "g": [1, 2, 3], "h": {"a": false, "b": 2, "c": 2.0, "d": "characters", "e": [1, 2, 3, 3], "f": [1, 2, 3, 3], "g": [1, 2, 3]}}'},
	)
	@Order(14)
	def testJSONDictionary(self, v, exp):
		encoded = SerializerHelper.Encode(v, format='json', charset='utf-8')
		decoded = SerializerHelper.Decode(encoded, format='json', charset='utf-8')
		ASSERT_IS_EQUAL(encoded, exp)
		return

