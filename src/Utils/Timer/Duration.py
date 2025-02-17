# -*- coding: utf-8 -*-

from .Timer import Timer
from .DurationTimer import DurationTimer

from functools import wraps

__all__ = (
	'Duration',
)


class Duration(object):

	TypeFunction = 0
	TypeMethod = 1
	TypeMethodClass = 2

	PARAM_KEYS_METHOD = ['self', 'this']
	PARAM_KEYS_METHOD_CLASS = ['cls', 'obj', 'o']

	def __init__(self, name : str = None, callback : callable = None) -> None:
		self.name = name
		self.callback = callback
		return
	
	def __call__(self, fn):
		self.fn = fn
		if not self.name:
			if isinstance(fn, property):
				self.name = fn.fget.__qualname__
			else:
				self.name = fn.__qualname__
		@wraps(fn)
		def decorator(*args, **kwargs):
			timer = DurationTimer()
			t = Timer()
			t.start()
			res = self.fn(*args, **kwargs)
			t.end()
			timer.add(self.name, t)
			if self.callback: self.callback(self.name, t.duration)
			return res
		return decorator
	