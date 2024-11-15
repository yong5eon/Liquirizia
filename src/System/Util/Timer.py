# -*- coding: utf-8 -*-

from threading import Timer as ThreadTimer

from typing import Callable

__all__ = (
	'SetTimer'
)


class Timer(object):
	def __init__(self, seconds: float, cb: Callable):
		self.timer = ThreadTimer(seconds, cb)
		return
	def start(self, *args, **kwds):
		self.timer.start()
		return
	def stop(self):
		self.timer.cancel()
		return
	

def SetTimer(seconds: float, cb: Callable):
	# TODO : in GNU/Linux, Mac OS, UNIX like, use signal with SIGALM OR SIGUSR
	timer = Timer(seconds, cb)
	timer.start()
	return timer
