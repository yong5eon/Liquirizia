# -*- coding: utf-8 -*-

from Liquirizia.Serializer import SerializerHelper, Serializer, Error

class SampleEncoder(Serializer):
	def __call__(self, obj):
		return str(obj)
	

class SampleDecoder(Serializer):
	def __call__(self, obj):
		return int(obj)
	

if __name__ == '__main__':

	helper = SerializerHelper()

	print(SerializerHelper.GetSupportFormats())

	SerializerHelper.Set('int', SampleEncoder, SampleDecoder)

	print(SerializerHelper.GetSupportFormats())

	encoded = SerializerHelper.Encode(0, format='int', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='int', charset='utf-8')
	print(encoded, decoded)

	serialized = SerializerHelper.Serialize(0, format='int')
	packed = SerializerHelper.Pack(serialized, charset='utf-8')
	print(serialized, packed)

	unpacked = SerializerHelper.Unpack(packed, charset='utf-8')
	deserialized = SerializerHelper.Deserialize(unpacked, format='int')
	print(unpacked, deserialized)
