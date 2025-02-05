# -*- coding: utf-8 -*-

from Liquirizia.System.Utils.Timer import SetTimer, Timeout, Timer, TimerCallback

from time import sleep


if __name__ == '__main__':

	class Callback(TimerCallback):
		def __init__(self, count: int = 1):
			self.count = count
			return
		def __call__(self, timer: Timer):
			if self.count != None:
				self.count -= 1
				if self.count != 0:
					timer.start()
			else:
				timer.start()
			print('Hello')
			return

	print('expect print hello after 100 ms, auto started')
	SetTimer(100, Callback()) # expect print hello after 100 ms, auto started
	sleep(1)

	print('expect print hello 3 times in every each 100 ms, auto started')
	SetTimer(100, Callback(3)) # expect print hello 3 times in every each 100 ms, auto started
	sleep(1)

	print('expect print hello until timer would be stopped in every each 100 ms, auto started')
	SetTimer(100, Callback(None)) # expect print hello until timer would be stopped in every each 100 ms, auto started
	sleep(1)

	def timeout_with_raise_exception():
		raise RuntimeError('timeout')
	
	def timeout_with_return():
		return 'timeout'

	@Timeout(100, timeout_with_raise_exception)
	def do_if_timeout_then_raise_exception(ms: int = None):
		if ms:
			sleep(ms / 1000)
		print('do if timeout then raise exception')
		return
	
	@Timeout(100, timeout_with_return)
	def do_if_timeout_return(ms: int = None):
		if ms:
			sleep(ms / 1000)
		return 'do if timeout then return'

	print('test raising exception when timeout')
	try:
		do_if_timeout_then_raise_exception(10) # expect print "do if timeout then raise exception"
		do_if_timeout_then_raise_exception(1000) # expect RuntimeError
	except RuntimeError as e:
		print(str(e))

	print('test returing when timeout')
	print(do_if_timeout_return(10)) # expect print "do if timeout then return"
	print(do_if_timeout_return(1000)) # expect print "timeout"

	class Sample(object):
		@Timeout(100, timeout_with_raise_exception)
		def do_if_timeout_then_raise_exception(self, ms: int = None):
			if ms:
				sleep(ms / 1000)
			print('do if timeout then raise exception')
			return
		
		@Timeout(100, timeout_with_return)
		def do_if_timeout_return(self, ms: int = None):
			if ms:
				sleep(ms / 1000)
			return 'do if timeout then return'

	print('test raising exception when timeout with class')
	try:
		_ = Sample()
		_.do_if_timeout_then_raise_exception(10) # expect print "do if timeout then raise exception"
		_.do_if_timeout_then_raise_exception(1000) # expect RuntimeError
	except RuntimeError as e:
		print(str(e))

	print('test returing when timeout with class')
	_ = Sample()
	print(_.do_if_timeout_return(10)) # expect print "do if timeout then return"
	print(_.do_if_timeout_return(1000)) # expect print "timeout"

