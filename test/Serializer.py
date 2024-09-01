# -*- coding: utf-8 -*-

from unittest import TestCase

from Liquirizia.Test import *

from Liquirizia.Serializer import SerializerHelper, Serializer


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
		{'v': 0, 'encoded': b'0'},
		{'v': 1, 'encoded': b'1'},
	)
	@Order(5)
	def testEncode(self, v, encoded):
		ASSERT_IS_EQUAL(SerializerHelper.Encode(v, format='int', charset='utf-8'), encoded)

	@Parameterized(
		{'v': b'0', 'decoded': 0},
		{'v': b'1', 'decoded': 1},
	)
	@Order(6)
	def testDecode(self, v, decoded):
		ASSERT_TRUE(SerializerHelper.Decode(v, format='int', charset='utf-8') == decoded) 

	@Parameterized(
		{'v': 0, 'serialized': '0'},
		{'v': 1, 'serialized': '1'},
	)
	@Order(1)
	def testSerialize(self, v, serialized):
		ASSERT_TRUE(SerializerHelper.Serialize(v, format='int') == serialized)

	@Parameterized(
		{'v': '0', 'deserialized': 0},
		{'v': '1', 'deserialized': 1},
	)
	@Order(2)
	def testDesrialize(self, v, deserialized):
		ASSERT_TRUE(SerializerHelper.Deserialize(v, format='int') == deserialized) 

	@Parameterized(
		{'v': '0', 'pack': b'0'},
		{'v': '1', 'pack': b'1'},
	)
	@Order(3)
	def testPack(self, v, pack):
		ASSERT_TRUE(SerializerHelper.Pack(v, charset='utf-8') == pack)

	@Parameterized(
		{'v': b'0', 'unpack': '0'},
		{'v': b'1', 'unpack': '1'},
	)
	@Order(4)
	def testUnpack(self, v, unpack):
		ASSERT_TRUE(SerializerHelper.Unpack(v, charset='utf-8') == unpack)
