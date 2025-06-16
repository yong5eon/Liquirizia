# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns.Type import *
from Liquirizia.Validator.Patterns.Compare import *

from decimal import Decimal
from dataclasses import dataclass, is_dataclass

class TestValidatorPatternsType(Case):

	@Order(1)
	def testIsTypeOf(self):
		va = Validator(IsTypeOf(int))
		ASSERT_IS_EQUAL(va(1), 1)
		ASSERT_IS_EQUAL(va(2), 2)
		with ASSERT_EXCEPT(TypeError):
			va('string')
		va = Validator(IsTypeOf(int, IsGreaterThan(0)))
		ASSERT_IS_EQUAL(va(1), 1)
		ASSERT_IS_EQUAL(va(2), 2)
		with ASSERT_EXCEPT(ValueError):
			va(-1)
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return
	
	@Order(2)
	def testIsBool(self):
		va = Validator(IsBool())
		ASSERT_IS_EQUAL(va(True), True)
		ASSERT_IS_EQUAL(va(False), False)
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return
	
	@Order(3)
	def testIsInteger(self):
		va = Validator(IsInteger())
		ASSERT_IS_EQUAL(va(1), 1)
		ASSERT_IS_EQUAL(va(2), 2)
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return
	
	@Order(4)
	def testIsFloat(self):
		va = Validator(IsFloat())
		ASSERT_IS_EQUAL(va(1.0), 1.0)
		ASSERT_IS_EQUAL(va(2.5), 2.5)
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return
	
	@Order(5)
	def testIsNumber(self):
		va = Validator(IsNumber())
		ASSERT_IS_EQUAL(va(1), 1)
		ASSERT_IS_EQUAL(va(2.5), 2.5)
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return
	
	@Order(6)
	def testIsString(self):
		va = Validator(IsString())
		ASSERT_IS_EQUAL(va('string'), 'string')
		ASSERT_IS_EQUAL(va('another string'), 'another string')
		with ASSERT_EXCEPT(TypeError):
			va(1)
		return
	
	@Order(7)
	def testIsList(self):
		va = Validator(IsList())
		ASSERT_IS_EQUAL(va([]), [])
		ASSERT_IS_EQUAL(va([1, 2, 3]), [1, 2, 3])
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return

	@Order(8)
	def testIsTuple(self):
		va = Validator(IsTuple())
		ASSERT_IS_EQUAL(va(()), ())
		ASSERT_IS_EQUAL(va((1, 2, 3)), (1, 2, 3))
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return
	
	@Order(9)
	def testIsSet(self):
		va = Validator(IsSet())
		ASSERT_IS_EQUAL(va(set()), set())
		ASSERT_IS_EQUAL(va({1, 2, 3}), {1, 2, 3})
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return
	
	@Order(10)
	def testIsArray(self):
		va = Validator(IsArray())
		ASSERT_IS_EQUAL(va([1, 2, 3]), [1, 2, 3])
		ASSERT_IS_EQUAL(va((1, 2, 3)), (1, 2, 3))
		ASSERT_IS_EQUAL(va({1, 2, 3}), {1, 2, 3})
		ASSERT_IS_EQUAL(va('string'), 'string')
		ASSERT_IS_EQUAL(va([1, 'string', 3.0]), [1, 'string', 3.0])
		return
	
	@Order(11)
	def testIsObject(self):
		va = Validator(IsObject())
		ASSERT_IS_EQUAL(va({}), {})
		ASSERT_IS_EQUAL(va({'key': 'value'}), {'key': 'value'})
		with ASSERT_EXCEPT(TypeError):
			va('string')
		with ASSERT_EXCEPT(TypeError):
			va([1, 2, 3])
		return
	
	@Order(12)
	def testIsByteArray(self):
		va = Validator(IsByteArray())
		ASSERT_IS_EQUAL(va(b'byte array'), b'byte array')
		ASSERT_IS_EQUAL(va(bytes([1, 2, 3])), bytes([1, 2, 3]))
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return
	
	@Order(13)
	def testIsByteStream(self):
		va = Validator(IsByteStream())
		ASSERT_IS_EQUAL(va(bytearray([1, 2, 3])), bytearray([1, 2, 3]))
		with ASSERT_EXCEPT(TypeError):
			va(b'bytes')
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return
	
	@Order(14)
	def testIsDecimal(self):
		va = Validator(IsDecimal())
		ASSERT_IS_EQUAL(va(Decimal('1.0')), Decimal('1.0'))
		ASSERT_IS_EQUAL(va(Decimal('2.5')), Decimal('2.5'))
		with ASSERT_EXCEPT(TypeError):
			va('string')
		return
	
	@Order(15)
	def testIsDataObject(self):
		@dataclass
		class DataObject:
			key: str
			value: int
		va = Validator(IsDataObject())
		ASSERT_IS_EQUAL(va(DataObject('key', 1)), DataObject('key', 1))
		ASSERT_IS_EQUAL(va(DataObject('another key', 2)), DataObject('another key', 2))
		with ASSERT_EXCEPT(TypeError):
			va('string')
		with ASSERT_EXCEPT(TypeError):
			va(1)
		with ASSERT_EXCEPT(TypeError):
			va({'key': 'value'})
		return
	
	@Order(101)
	def testToTypeOf(self):
		va = Validator(ToTypeOf(int))
		ASSERT_IS_EQUAL(va(1), 1)
		ASSERT_IS_EQUAL(va('2'), 2)
		with ASSERT_EXCEPT(ValueError):
			va('string')
		va = Validator(ToTypeOf(float))
		ASSERT_IS_EQUAL(va(1), 1.0)
		ASSERT_IS_EQUAL(va('2.5'), 2.5)
		with ASSERT_EXCEPT(ValueError):
			va('string')
		return
	
	@Order(102)
	def testToBool(self):
		va = Validator(ToBool())
		ASSERT_IS_EQUAL(va(True), True)
		ASSERT_IS_EQUAL(va(False), False)
		ASSERT_IS_EQUAL(va('True'), True)
		ASSERT_IS_EQUAL(va('False'), False)
		ASSERT_IS_EQUAL(va('1'), True)
		ASSERT_IS_EQUAL(va('0'), False)
		ASSERT_IS_EQUAL(va(1), True)
		ASSERT_IS_EQUAL(va(0), False)
		with ASSERT_EXCEPT(ValueError):
			va('string')
		return
	
	@Order(103)
	def testToInteger(self):
		va = Validator(ToInteger())
		ASSERT_IS_EQUAL(va(1), 1)
		ASSERT_IS_EQUAL(va('2'), 2)
		ASSERT_IS_EQUAL(va('3.0'), 3)
		with ASSERT_EXCEPT(ValueError):
			va('string')
		return
	
	@Order(104)
	def testToFloat(self):
		va = Validator(ToFloat())
		ASSERT_IS_EQUAL(va(1), 1.0)
		ASSERT_IS_EQUAL(va('2.5'), 2.5)
		ASSERT_IS_EQUAL(va('3'), 3.0)
		with ASSERT_EXCEPT(ValueError):
			va('string')
		return
	
	@Order(105)
	def testToString(self):
		va = Validator(ToString())
		ASSERT_IS_EQUAL(va('string'), 'string')
		ASSERT_IS_EQUAL(va(1), '1')
		ASSERT_IS_EQUAL(va(2.5), '2.5')
		return
	
	@Order(106)
	def testToList(self):
		va = Validator(ToList())
		ASSERT_IS_EQUAL(va([]), [])
		ASSERT_IS_EQUAL(va([1, 2, 3]), [1, 2, 3])
		ASSERT_IS_EQUAL(va((1, 2, 3)), [1, 2, 3])
		ASSERT_IS_EQUAL(va('string'), ['s', 't', 'r', 'i', 'n', 'g'])
		return
	
	@Order(107)
	def testToTuple(self):
		va = Validator(ToTuple())
		ASSERT_IS_EQUAL(va(()), ())
		ASSERT_IS_EQUAL(va([1, 2, 3]), (1, 2, 3))
		ASSERT_IS_EQUAL(va((1, 2, 3)), (1, 2, 3))
		ASSERT_IS_EQUAL(va('string'), ('s', 't', 'r', 'i', 'n', 'g'))
		return
	
	@Order(108)
	def testToSet(self):
		va = Validator(ToSet())
		ASSERT_IS_EQUAL(va(set()), set())
		ASSERT_IS_EQUAL(va([1, 2, 3]), {1, 2, 3})
		ASSERT_IS_EQUAL(va((1, 2, 3)), {1, 2, 3})
		ASSERT_IS_EQUAL(va('string'), {'s', 't', 'r', 'i', 'n', 'g'})
		return

	@Order(109)
	def testToObject(self):
		va = Validator(ToObject())
		ASSERT_IS_EQUAL(va({}), {})
		ASSERT_IS_EQUAL(va({'key': 'value'}), {'key': 'value'})
		ASSERT_IS_EQUAL(va([('key', 'value')]), {'key': 'value'})
		with ASSERT_EXCEPT(ValueError):
			va('string')
		return
	
	@Order(110)
	def testToByteArray(self):
		va = Validator(ToByteArray())
		ASSERT_IS_EQUAL(va(b'byte array'), b'byte array')
		ASSERT_IS_EQUAL(va(bytes([1, 2, 3])), bytes([1, 2, 3]))
		with ASSERT_EXCEPT(ValueError): va('string')
		return
	
	@Order(111)
	def testToByteStream(self):
		va = Validator(ToByteStream())
		ASSERT_IS_EQUAL(va(bytearray([1, 2, 3])), bytearray([1, 2, 3]))
		ASSERT_IS_EQUAL(va(b'bytes'), bytearray(b'bytes'))
		with ASSERT_EXCEPT(ValueError): va('string')
		return
	
	@Order(112)
	def testToDecimal(self):
		va = Validator(ToDecimal())
		ASSERT_IS_EQUAL(va(Decimal('1.0')), Decimal('1.0'))
		ASSERT_IS_EQUAL(va('2.5'), Decimal('2.5'))
		ASSERT_IS_EQUAL(va('3'), Decimal('3'))
		with ASSERT_EXCEPT(ValueError):
			va('string')
		return
	
	@Order(113)
	def testToDataObject(self):
		@dataclass
		class DataObject:
			key: str
			value: int
		va = Validator(ToDataObject())
		ASSERT_IS_EQUAL(is_dataclass(va({'key': 'key', 'value': 2})), True)
		with ASSERT_EXCEPT(ValueError):
			va('string')
		with ASSERT_EXCEPT(ValueError):
			va(1)
		return
	