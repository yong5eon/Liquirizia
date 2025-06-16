# -*- coding: utf-8 -*-

from threading import Timer as ThreadTimer
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
		def cb():
			return self.cb(self)
		self.timer = ThreadTimer(self.ms / 1000, cb)
		self.timer.start()
		return
	def stop(self):
		self.timer.cancel()
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
				from signal import raise_signal, SIGINT
				raise_signal(SIGINT)
				return
			try:
				timer = SetTimer(self.timeout, cb)
				return fn(*args, **kwargs)
			except KeyboardInterrupt:
				return self.cb()
			finally:
				timer.stop()
		return wrapper
