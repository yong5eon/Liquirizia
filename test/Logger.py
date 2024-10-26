# -*- coding: utf-8 -*-

from Liquirizia.Test import *
from Liquirizia.Logger import *


class TestLogger(Case):
	@classmethod
	def setUpClass(cls) -> None:
		LOG_INIT('DEBUG')
		return super().setUpClass()

	@Parameterized(
			{'v': 'TEST DEBUG LOG'},
			{'v': 'TEST DEBUG LOG'},
			{'v': 'TEST DEBUG LOG'},
	)
	@Order(0)
	def testDebug(self, v):
		with ASSERT_WITH_LOG(level='DEBUG') as log:
			LOG_DEBUG(v)
			ASSERT_IS_EQUAL(len(log.output), 1)
			ASSERT_IS_EQUAL(len(log.records), 1)
			ASSERT_IS_IN(v, log.output[0])
		return

	@Parameterized(
			{'v': 'TEST INFO LOG'},
			{'v': 'TEST INFO LOG'},
			{'v': 'TEST INFO LOG'},
	)
	@Order(1)
	def testInfo(self, v):
		with ASSERT_WITH_LOG(level='INFO') as log:
			LOG_INFO(v)
			ASSERT_IS_EQUAL(len(log.output), 1)
			ASSERT_IS_EQUAL(len(log.records), 1)
			ASSERT_IS_IN(v, log.output[0])
		return

	@Parameterized(
			{'v': 'TEST WARN LOG'},
			{'v': 'TEST WARN LOG'},
			{'v': 'TEST WARN LOG'},
	)
	@Order(2)
	def testWarn(self, v):
		with ASSERT_WITH_LOG(level='WARN') as log:
			LOG_WARN(v)
			ASSERT_IS_EQUAL(len(log.output), 1)
			ASSERT_IS_EQUAL(len(log.records), 1)
			ASSERT_IS_IN(v, log.output[0])
		return

	@Parameterized(
			{'v': 'TEST ERROR LOG'},
			{'v': 'TEST ERROR LOG'},
			{'v': 'TEST ERROR LOG'},
	)
	@Order(3)
	def testError(self, v):
		with ASSERT_WITH_LOG(level='ERROR') as log:
			LOG_ERROR(v)
			ASSERT_IS_EQUAL(len(log.output), 1)
			ASSERT_IS_EQUAL(len(log.records), 1)
			ASSERT_IS_IN(v, log.output[0])
		return

