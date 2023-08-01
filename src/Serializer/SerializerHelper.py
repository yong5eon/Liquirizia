# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .Errors import *

__all__ = (
	'SerializerHelper'
)


class SerializerHelper(Singleton):
	"""
	Serializer Helper Class
	"""
	def __init__(self):
		self.serializers = {}
		return

	@classmethod
	def Set(cls, format, encoder, decoder):
		helper = cls()
		helper.set(
			format,
			encoder=encoder,
			decoder=decoder
		)
		return

	def set(self, format, encoder, decoder):
		self.serializers[format.lower()] = (encoder, decoder)
		return

	@classmethod
	def Get(cls, format):
		helper = cls()
		return helper.get(format)

	def get(self, format):
		if not format:
			return None, None

		encoder, decoder = self.serializers.get(format.lower(), (None, None))

		if not encoder or not decoder:
			raise NotSupportedError(format)

		return encoder(), decoder()

	@classmethod
	def GetEncoder(cls, format):
		helper = cls()
		return helper.encoder(format)

	def encoder(self, format):
		encoder, decoder = self.get(format)
		return encoder

	@classmethod
	def GetDecoder(cls, format):
		helper = cls()
		return helper.decoder(format)

	def decoder(self, format):
		encoder, decoder = self.get(format)
		return decoder

	@classmethod
	def Encode(cls, value, format=None, charset=None):
		helper = cls()
		return helper.encode(value, format, charset)

	def encode(self, value, format=None, charset=None):
		if not format:
			return str(value).encode(charset) if charset else str(value).encode()

		serializer = self.encoder(format)

		if not serializer:
			raise NotSupportedError(format)

		try:
			return serializer(value).encode(charset) if charset else serializer(value).encode()
		except BaseException as e:
			raise EncodeError(value, format, charset, e)

	@classmethod
	def Decode(cls, value, format=None, charset=None):
		helper = cls()
		return helper.decode(value, format, charset)

	def decode(self, value, format=None, charset=None):
		if not isinstance(value, (bytes, bytearray)):
			raise DecodeError(value, format, charset, RuntimeError('{} is not bytes or bytearray'.format(value)))

		if not format:
			return value.decode(charset) if charset else value.decode()

		serializer = self.decoder(format)

		if not serializer:
			raise NotSupportedError(format)

		try:
			return serializer(value.decode(charset) if charset else value.decode())
		except BaseException as e:
			raise DecodeError(value, format, charset, e)
		
	@classmethod
	def Serialize(cls, value, format=None):
		helper = cls()
		return helper.serialize(value, format)

	def serialize(self, value, format=None):
		serializer = self.encoder(format)
		if not serializer:
			raise NotSupportedError(format)
		return serializer(value)
	
	@classmethod
	def Deserialize(cls, value, format=None):
		helper = cls()
		return helper.deserialize(value, format)

	def deserialize(self, value, format=None):
		serializer = self.decoder(format)
		if not serializer:
			raise NotSupportedError(format)
		return serializer(value)

	@classmethod
	def Pack(cls, value, charset=None):
		helper = cls()
		return helper.pack(value, charset)

	def pack(self, value, charset=None):
		return value.encode(charset) if charset else value.encode()
	
	@classmethod
	def Unpack(cls, value, charset=None):
		helper = cls()
		return helper.unpack(value, charset)

	def unpack(self, value, charset=None):
		return value.decode(charset) if charset else value.decode()
