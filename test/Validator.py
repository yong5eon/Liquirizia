# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validate, Validator, Pattern
from Liquirizia.Validator.Patterns import *
from Liquirizia.Validator.Patterns.Array import *
from Liquirizia.Validator.Patterns.Dictionary import (
	IsRequiredIn as IsRequiredInDictionary,
	IsMappingOf as IsMappingOfDictionary,
)
from Liquirizia.Validator.Patterns.DataObject import (
	IsRequiredIn as IsRequiredInDataObject,
	IsMappingOf as IsMappingOfDataObject,
)

from dataclasses import dataclass

class TestValidator(Case):

	@Order(1)
	def testValidateType(self):
		va = Validator(IsBool())
		ASSERT_IS_EQUAL(va(True), True)
		with ASSERT_EXCEPT(TypeError):
			v = va(False)
			v = va(0)
			v = va(0.)
			v = va('Hi')
			v = va([])
			v = va(())
			v = va({})
			v = va(object())
		va = Validator(IsInteger())
		ASSERT_IS_EQUAL(va(1), True)
		with ASSERT_EXCEPT(TypeError):
			v = va(False)
			v = va(0)
			v = va(0.)
			v = va('Hi')
			v = va([])
			v = va(())
			v = va({})
			v = va(object())
		va = Validator(IsFloat())
		ASSERT_IS_EQUAL(va(0.), 0.)
		with ASSERT_EXCEPT(TypeError):
			v = va(False)
			v = va(0)
			v = va(0.)
			v = va('Hi')
			v = va([])
			v = va(())
			v = va({})
			v = va(object())
		va = Validator(IsString())
		ASSERT_IS_EQUAL(va('Hi'), 'Hi')
		with ASSERT_EXCEPT(TypeError):
			v = va(False)
			v = va(0)
			v = va(0.)
			v = va('Hi')
			v = va([])
			v = va(())
			v = va({})
			v = va(object())
		va = Validator(IsList())
		ASSERT_IS_EQUAL(va([]), [])
		with ASSERT_EXCEPT(TypeError):
			v = va(False)
			v = va(0)
			v = va(0.)
			v = va('Hi')
			v = va([])
			v = va(())
			v = va({})
			v = va(object())
		va = Validator(IsTuple())
		ASSERT_IS_EQUAL(va(()), ())
		with ASSERT_EXCEPT(TypeError):
			v = va(False)
			v = va(0)
			v = va(0.)
			v = va('Hi')
			v = va([])
			v = va(())
			v = va({})
			v = va(object())
		va = Validator(IsDictionary())
		ASSERT_IS_EQUAL(va({}), {})
		with ASSERT_EXCEPT(TypeError):
			v = va(False)
			v = va(0)
			v = va(0.)
			v = va('Hi')
			v = va([])
			v = va(())
			v = va({})
			v = va(object())
		va = Validator(IsDataObject())
		@dataclass
		class DataObject: pass
		_ = DataObject()
		ASSERT_IS_EQUAL(va(_), _)
		with ASSERT_EXCEPT(TypeError):
			v = va(False)
			v = va(0)
			v = va(0.)
			v = va('Hi')
			v = va([])
			v = va(())
			v = va({})
			v = va(object())
		return

	@Parameterized(
			{'input': 2, 'success': 2, 'fail': 3},
	)
	@Order(2)	
	def testValidateValueWithCustomizedPattern(self, input, success, fail):
		class TestPattern(Pattern):
			def __init__(self, success):
				self.success = success
				return
			def __call__(self, parameter):
				if parameter == self.success:
					return parameter + self.success
				raise ValueError('{} is not equal to {}'.format(parameter, self.success))
		va = Validator(TestPattern(success))
		ASSERT_IS_EQUAL(va(input), input + success)
		with ASSERT_EXCEPT(ValueError):
			fail = va(fail)
		return
	
	@Order(11)
	def testValidateList(self):
		class IsOver(Pattern):
			def __init__(self, base):
				self.base = base
				return
			def __call__(self, parameter):
				if not parameter > self.base:
					raise ValueError('{} is not over {}'.format(parameter, self.base))
				return parameter
		va = Validator(
			IsList(IsElementOf(IsOver(0)))
		)
		ASSERT_IS_EQUAL(va([1,2,3]), [1,2,3])
		with ASSERT_EXCEPT(TypeError):
			va(None)
		with ASSERT_EXCEPT(ValueError):
			va([])
			va([0,1,2,3])
		return

	@Order(12)
	def testValidateDictionary(self):
		class IsOver(Pattern):
			def __init__(self, base):
				self.base = base
				return
			def __call__(self, parameter):
				if not parameter > self.base:
					raise ValueError('{} is not over {}'.format(parameter, self.base))
				return parameter
		va = Validator(
			IsDictionary(
				IsRequiredInDictionary('a', 'b', 'c', 'd'),
				IsMappingOfDictionary({
					'a': Validator(IsNotToNone()),
					'b': Validator(IsNotToNone(), IsEqualTo(2)),
					'c': Validator(IsNotToNone(), IsIn(3, 4, 5, 6, 7, 8)),
					'd': Validator(SetDefault(4)),
					'e': Validator(IsArray(IsElementOf(IsOver(3)))),
					'f': Validator(IsDictionary(
						IsNotEmpty(),
						IsRequiredInDictionary('a', 'b'),
						IsMappingOfDictionary({
							'a': (IsNotToNone()),
							'b': (IsNotToNone(), IsOver(9)),
						})
					)),
				})
			)
		)
		s = {
			'a': 1,
			'b': 2,
			'c': 3,
			'd': None,
			'e': [4, 5, 6],
			'f': {
				'a': 10,
				'b': 11,
				'c': 12
			},
		}
		ASSERT_IS_EQUAL(va(s), s)
		with ASSERT_EXCEPT(TypeError):
			va(None)
		with ASSERT_EXCEPT(ValueError):
			va({})
			va({
				'a': 1,
				'b': 2,
				'd': None,
				'e': [4, 5, 6],
				'f': {
					'a': 10,
					'b': 11,
					'c': 12
				},
			})
		return
	
	@Order(13)
	def testValidateDataObject(self):
		class IsOver(Pattern):
			def __init__(self, base):
				self.base = base
				return
			def __call__(self, parameter):
				if not parameter > self.base:
					raise ValueError('{} is not over {}'.format(parameter, self.base))
				return parameter
		va = Validator(
			IsDataObject(
				IsRequiredInDataObject('a', 'b', 'c', 'd'),
				IsMappingOfDataObject({
					'a': Validator(),
					'b': Validator(IsEqualTo(2)),
					'c': Validator(IsIn(3, 4, 5, 6, 7, 8)),
					'd': Validator(SetDefault(4)),
					'e': Validator(IsArray(IsElementOf(IsOver(3)))),
					'f': Validator(IsDictionary(
						IsRequiredInDictionary('a', 'b'),
						IsMappingOfDictionary({
							'a': IsInteger(),
							'b': IsInteger(IsOver(9)),
						})
					)),
				})
			)
		)
		@dataclass
		class DataObject:
			a: int
			b: int
			c: int
			e: list
			f: dict
			d: int = None
		_ = DataObject(1, 2, 3, e=[4, 5, 6], f={'a': 10, 'b': 11, 'c': 12})
		ASSERT_IS_EQUAL(va(_), _)
		with ASSERT_EXCEPT(TypeError):
			va(None)
		with ASSERT_EXCEPT(TypeError):
			va({})
		with ASSERT_EXCEPT(ValueError):
			va(DataObject(
				a=1,
				b=2,
				c=None,
				d=4,
				e=[4, 5, 6],
				f={'a': 10, 'b': 11, 'c': 12},
			))
		return

	@Order(80)
	def testValidateDecoratorWithFunction(self):
		@Validate({
			'a': IsNotToNone(),
			'b': (IsNotToNone(), IsGreaterEqualTo(0)),
			'c': IsNotToNone(),
			'd': (IsNotToNone(), IsLessEqualTo(10)),
			'e': (IsArray(IsNotEmpty(), IsElementOf(IsLessThan(5)))),
			'f': IsDictionary(
				IsNotEmpty(),
				IsRequiredInDictionary('a', 'b'),
				IsMappingOfDictionary({
					'a': (IsNotToNone(), IsGreaterThan(0), IsLessThan(5)),
				})
			),
			'const': SetDefault(3),
		})
		def foo(a, b, c, d, e, f, const=None):
			return round((a + b + c + d) * sum(e) / sum(f.values()) % const)
		ASSERT_IS_EQUAL(foo(1, 2, 3, d=4, e=(1, 2, 3), f={'a': 2, 'b': 1}), 2)
		with ASSERT_EXCEPT(ValueError):
			foo(1, None, 3, d=4, e=(1, 2, 3), f={'a': 2, 'b': 1})
		return

	@Order(90)
	def testValidateDecoratorWithMethodOfClass(self):
		class O:
			@Validate({
				'a': IsNotToNone(),
				'b': (IsNotToNone(), IsGreaterEqualTo(0)),
				'c': IsNotToNone(),
				'd': (IsNotToNone(), IsLessEqualTo(10)),
				'e': (IsArray(IsNotEmpty(), IsElementOf(IsLessThan(5)))),
				'f': 
				IsDictionary(
					IsNotEmpty(),
					IsMappingOfDictionary({
						'a': (IsNotToNone(), IsGreaterThan(0), IsLessThan(5)),
					})
				)
				,
				'const': SetDefault(3),
			})
			def foo(self, a, b, c, d, e, f, const=None):
				return round((a + b + c + d) * sum(e) / sum(f.values()) % const)
		o = O()
		ASSERT_IS_EQUAL(o.foo(1, 2, 3, d=4, e=(1, 2, 3), f={'a': 2, 'b': 1}), 2)
		with ASSERT_EXCEPT(ValueError):
			o.foo(1, None, 3, d=4, e=(1, 2, 3), f={'a': 2, 'b': 1})
		return
