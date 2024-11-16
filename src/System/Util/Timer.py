# -*- coding: utf-8 -*-

from platform import system


from typing import Callable

__all__ = (
	'SetTimer',
	'Timeout',
)


class Timer(object):
	def __init__(self, ms: int, cb: Callable):
		self.cb = cb
		self.ms = ms
		return
	def start(self):
		if system().upper() == 'WINDOWS':
			from threading import Timer as ThreadTimer
			self.timer = ThreadTimer(self.ms / 1000, self.cb)
			self.timer.start()
		else:
			from signal import signal, SIGALRM, setitimer, ITIMER_REAL
			def callback(sig, frame):
				return self.cb()
			self.timer = signal(SIGALRM, callback)
			setitimer(ITIMER_REAL, self.ms / 1000, 0.0)	
		return
	def stop(self):
		if system().upper() == 'WINDOWS':
			self.timer.cancel()
		else:
			from signal import signal, SIGALRM, SIG_DFL
			signal(SIGALRM, SIG_DFL)
		return
	

def SetTimer(ms: int, cb: Callable):
	timer = Timer(ms, cb)
	timer.start()
	return timer


class Timeout(object):
	def __init__(
		self,
		timeout: int,
		cb: Callable,
	):
		self.timeout = timeout
		self.cb = cb
		return
	def __call__(self, fn: Callable):
		def wrapper(*args, **kwargs):
			timer = Timer(self.timeout, self.cb)
			timer.start()
			_ = fn(*args, **kwargs)
			timer.stop()
			return _
		return wrapper
