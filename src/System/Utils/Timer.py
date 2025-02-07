# -*- coding: utf-8 -*-

from platform import system
from functools import wraps
from abc import ABCMeta, abstractmethod
from typing import Callable

__all__ = (
	'SetTimer',
	'Timer',
	'TimerCallback',
	'Timeout',
)


class TimerCallback(metaclass=ABCMeta):
	"""Timer Callback Interface"""
	@abstractmethod
	def __call__(self, timer: 'Timer'):
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))


class Timer(object):
	"""Timer Class"""
	def __init__(self, ms: int, cb: TimerCallback):
		self.cb = cb
		self.ms = ms
		self.timer = None
		return
	def start(self):
		if system().upper() == 'WINDOWS':
			from ctypes import windll, WINFUNCTYPE
			from ctypes.wintypes import UINT, DWORD, ULONG
			timeSetEvent = windll.winmm.timeSetEvent
			timeKillEvent = windll.winmm.timeKillEvent
			TIME_PERIODIC = 1
			TIME_CALLBACK_FUNCTION = 0x0000
			TIME_PROC = WINFUNCTYPE(None, UINT, UINT, DWORD, DWORD, DWORD)
			def cb(id, msg, user, dw1, dw2):
				timeKillEvent(id)
				return self.cb(self)
			self.rcb = TIME_PROC(cb)
			self.timer = timeSetEvent(
				UINT(self.ms),
				UINT(0),
				self.rcb,
				ULONG(0),
				UINT(TIME_CALLBACK_FUNCTION),
			)
		else:
			from signal import signal, SIGALRM, setitimer, ITIMER_REAL
			def cb(sig, frame):
				return self.cb(self)
			self.timer = signal(SIGALRM, cb)
			setitimer(ITIMER_REAL, self.ms / 1000, 0.0)	
		return
	def stop(self):
		if system().upper() == 'WINDOWS':
			from ctypes import windll
			timeKillEvent = windll.winmm.timeKillEvent
			timeKillEvent(self.timer)
		else:
			from signal import signal, SIGALRM, SIG_DFL
			signal(SIGALRM, SIG_DFL)
		self.timer = None
		return
	

def SetTimer(ms: int, cb: TimerCallback, start: bool = True):
	"""Set Timer Function"""
	timer = Timer(ms, cb)
	if start:
		timer.start()
	return timer


class Timeout(object):
	"""Timeout Decorator"""
	def __init__(
		self,
		timeout: int,
		cb: Callable,
	):
		self.timeout = timeout
		self.cb = cb
		return
	def __call__(self, fn: Callable):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			def cb(timer: Timer):
				raise TimeoutError()
			try:
				SetTimer(self.timeout, cb)
				return fn(*args, **kwargs)
			except TimeoutError:
				return self.cb()
		return wrapper
