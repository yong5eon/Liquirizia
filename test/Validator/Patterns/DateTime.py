# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns.DateTime import *

from datetime import datetime, date, time

class TestValidatorPatternsDateTime(Case):

	@Order(1)
	def testIsDateTime(self):
		va = Validator(IsDateTime())
		ASSERT_IS_EQUAL(va(datetime(2023, 10, 1, 12, 0)), datetime(2023, 10, 1, 12, 0))
		with ASSERT_EXCEPT(TypeError):
			va('2023-10-01 12:00')
		return
	
	@Order(2)
	def testIsDate(self):
		va = Validator(IsDate())
		ASSERT_IS_EQUAL(va(date(2023, 10, 1)), date(2023, 10, 1))
		with ASSERT_EXCEPT(TypeError):
			va('2023-10-01')
		return
	
	@Order(3)
	def testIsTime(self):
		va = Validator(IsTime())
		ASSERT_IS_EQUAL(va(time(12, 0)), time(12, 0))
		with ASSERT_EXCEPT(TypeError):
			va('12:00')
		return
	
	@Order(4)
	def testToDateTime(self):
		va = Validator(ToDateTime())
		ASSERT_IS_EQUAL(va('2023-10-01 12:00:00'), datetime(2023, 10, 1, 12, 0, 0))
		with ASSERT_EXCEPT(ValueError):
			va('2023-10')
		with ASSERT_EXCEPT(ValueError):
			va(datetime(2023, 10, 1, 12, 0))
		return
	
	@Order(5)
	def testToDate(self):
		va = Validator(ToDate())
		ASSERT_IS_EQUAL(va('2023-10-01'), date(2023, 10, 1))
		with ASSERT_EXCEPT(ValueError):
			va('2023-10-01 12:00:00')
		with ASSERT_EXCEPT(ValueError):
			va(date(2023, 10, 1))
		return
	
	@Order(6)
	def testToTime(self):
		va = Validator(ToTime())
		ASSERT_IS_EQUAL(va('12:00:00'), time(12, 0, 0))
		with ASSERT_EXCEPT(ValueError):
			va('1231231')
		with ASSERT_EXCEPT(ValueError):
			va(time(12, 0, 0))
		return
