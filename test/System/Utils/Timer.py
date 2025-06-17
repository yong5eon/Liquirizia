# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.System.Utils import SetTimer, Timeout, TimerCallback, Timer
from time import sleep


class TestSystemUtilsTimer(Case):
	@Order(0)
	def testSetTimer(self):
		class Callback(TimerCallback):
			def __init__(self, data: list, count: int = 1):
				self.data = data
				self.count = count
				return
			def __call__(self, timer: Timer):
				self.data.append(self.count)
				if self.count != None:
					self.count -= 1
					if self.count != 0:
						timer.start()
				else:
					timer.start()
				return
		_ = []
		SetTimer(10, Callback(_))
		sleep(1)
		ASSERT_IS_EQUAL(len(_), 1)
		_ = []
		SetTimer(10, Callback(_, 3))
		sleep(1)
		ASSERT_IS_EQUAL(len(_), 3)
		return

	@Order(1)
	def testTimeoutDecorator(self):
		def timeout_with_raise_exception():
			raise RuntimeError('timeout')
		def timeout_with_return():
			return 0

		@Timeout(300, timeout_with_raise_exception)
		def do_if_timeout_then_raise_exception(ms: int = None):
			if ms:
				sleep(ms / 1000)
			return 1
		
		with ASSERT_EXCEPT(RuntimeError) as ctx:
			ASSERT_IS_EQUAL(do_if_timeout_then_raise_exception(10), 1)
			do_if_timeout_then_raise_exception(1000)
		ASSERT_IS_EQUAL(isinstance(ctx.exception, RuntimeError), True)

		@Timeout(300, timeout_with_return)
		def do_if_timeout_return(ms: int = None):
			if ms:
				sleep(ms / 1000)
			return 1
		
		ASSERT_IS_EQUAL(do_if_timeout_return(10), 1)
		ASSERT_IS_EQUAL(do_if_timeout_return(1000), 0)
		return

	@Order(2)
	def testTimeoutDecoratorWithClass(self):
		def timeout_with_raise_exception():
			raise RuntimeError('timeout')
		def timeout_with_return():
			return 0
		class Sample(object):
			@Timeout(100, timeout_with_raise_exception)
			def do_if_timeout_then_raise_exception(self, ms: int = None):
				if ms:
					sleep(ms / 1000)
				return 1
			@Timeout(100, timeout_with_return)
			def do_if_timeout_return(self, ms: int = None):
				if ms:
					sleep(ms / 1000)
				return 1
			
		_ = Sample()

		with ASSERT_EXCEPT(RuntimeError) as ctx:
			ASSERT_IS_EQUAL(_.do_if_timeout_then_raise_exception(10), 1)
			_.do_if_timeout_then_raise_exception(1000)
		ASSERT_IS_EQUAL(isinstance(ctx.exception, RuntimeError), True)

		ASSERT_IS_EQUAL(_.do_if_timeout_return(10), 1)
		ASSERT_IS_EQUAL(_.do_if_timeout_return(1000), 0)
		return
