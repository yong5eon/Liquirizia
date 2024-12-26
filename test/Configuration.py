# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.Configuration import Configuration, Value, Handler

from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import IsString

from typing import List
import os

class TestSampleConfiguration(Case):

	@Order(0)
	def testDefaultValues(self):
		class Settings(Configuration):
			MODE: str = Value('MODE', default='DEBUG', va=Validator(IsString()))
			LOG_LEVEL: str = 'DEBUG'
			LOG_NAME: str = 'WORKER'
			TIMEZONE: str = 'Asia/Seoul'

		_ = Settings()
		ASSERT_IS_EQUAL(_.MODE, 'DEBUG')
		ASSERT_IS_EQUAL(_.LOG_LEVEL, 'DEBUG')
		ASSERT_IS_EQUAL(_.LOG_NAME, 'WORKER')
		ASSERT_IS_EQUAL(_.TIMEZONE, 'Asia/Seoul')
		return

	@Order(1)
	def testModifyValues(self):
		class Settings(Configuration):
			MODE: str = Value('MODE', default='DEBUG', va=Validator(IsString()))
			LOG_LEVEL: str = 'DEBUG'
			LOG_NAME: str = 'WORKER'
			TIMEZONE: str = 'Asia/Seoul'

		_ = Settings()
		_.MODE = 'PRODUCTION'
		ASSERT_IS_EQUAL(_.MODE, 'PRODUCTION')
		return

	@Order(2)
	def testMultipleInstances(self):
		class Settings(Configuration):
			MODE: str = Value('MODE', default='DEBUG', va=Validator(IsString()))
			LOG_LEVEL: str = 'DEBUG'
			LOG_NAME: str = 'WORKER'
			TIMEZONE: str = 'Asia/Seoul'

		a = Settings()
		a.MODE = 'PRODUCTION'
		b = Settings()
		b.LOG_NAME = 'TEST_WORKER'

		ASSERT_IS_EQUAL(a.MODE, 'PRODUCTION')
		ASSERT_IS_EQUAL(b.MODE, 'PRODUCTION')
		ASSERT_IS_EQUAL(a.LOG_NAME, 'TEST_WORKER')
		ASSERT_IS_EQUAL(b.LOG_NAME, 'TEST_WORKER')
		return

	@Order(3)
	def testEnvironmentVariables(self):
		os.environ['MODE'] = 'TEST'
		os.environ['LOG_LEVEL'] = 'INFO'
		os.environ['LOG_NAME'] = 'TEST_WORKER'
		os.environ['TIMEZONE'] = 'UTC'

		class Settings(Configuration):
			MODE: str = Value('MODE', default='DEBUG', va=Validator(IsString()))
			LOG_LEVEL: str = 'DEBUG'
			LOG_NAME: str = 'WORKER'
			TIMEZONE: str = 'Asia/Seoul'

		_ = Settings()
		ASSERT_IS_EQUAL(_.MODE, 'TEST')
		ASSERT_IS_EQUAL(_.LOG_LEVEL, 'INFO')
		ASSERT_IS_EQUAL(_.LOG_NAME, 'TEST_WORKER')
		ASSERT_IS_EQUAL(_.TIMEZONE, 'UTC')

		# Clean up environment variables
		del os.environ['MODE']
		del os.environ['LOG_LEVEL']
		del os.environ['LOG_NAME']
		del os.environ['TIMEZONE']
		return

	@Order(4)
	def testHandlers(self):
		class PreLoadHandler(Handler):
			def __call__(self, conf: Configuration):
				conf.LOG_NAME = 'PRELOAD'
				return
	
		class PostLoadHandler(Handler):
			def __call__(self, conf: Configuration):
				conf.LOG_NAME = 'POSTLOAD'
				return

		class Settings(Configuration, onLoad=PreLoadHandler(), onLoaded=PostLoadHandler()):
			MODE: str = Value('MODE', default='DEBUG', va=Validator(IsString()))
			LOG_LEVEL: str = 'DEBUG'
			LOG_NAME: str = 'WORKER'
			TIMEZONE: str = 'Asia/Seoul'

		_ = Settings()
		ASSERT_IS_EQUAL(_.LOG_NAME, 'POSTLOAD')
		return
