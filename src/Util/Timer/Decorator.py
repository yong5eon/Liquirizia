# -*- coding: utf-8 -*-

from .Timer import Timer
from .DurationTimer import DurationTimer

from functools import wraps

__all__ = (
	'Duration',
)


class Decorator(object):

	TypeFunction = 0
	TypeMethod = 1
	TypeMethodClass = 2

	PARAM_KEYS_METHOD = ['self', 'this']
	PARAM_KEYS_METHOD_CLASS = ['cls', 'obj', 'o']

	def __init__(self, fn, name : str = None, callback : callable = None) -> None:
		self.fn = fn
		if name:
			self.name = name
		else:
			if isinstance(fn, property):
				self.name = fn.fget.__qualname__
			else:
				self.name = fn.__qualname__
		self.callback = callback
		return
	
	def __get__(self, instance, owner):
		if isinstance(self.fn, staticmethod):
			return lambda *args, **kwargs: self.__call_method_static__(self.fn.__func__, *args, **kwargs)
		if isinstance(self.fn, classmethod):
			return lambda *args, **kwargs: self.__call_method_class__(self.fn.__func__, owner, *args, **kwargs)
		if isinstance(self.fn, property):
			return self.__call_property__(self.fn, instance)
		return lambda *args, **kwargs: self.__call_method__(self.fn, instance, *args, **kwargs)

	def __call__(self, *args, **kwargs):
		timer = DurationTimer()
		t = Timer()
		t.start()
		res = self.fn(*args, **kwargs)
		t.end()
		timer.add(self.name, t)
		if self.callback: self.callback(self.name, t.duration)
		return res
	
	def __call_method_static__(self, fn, *args, **kwargs):
		timer = DurationTimer()
		t = Timer()
		t.start()
		res = fn(*args, **kwargs)
		t.end()
		timer.add(self.name, t)
		if self.callback: self.callback(self.name, t.duration)
		return res
	
	def __call_method_class__(self, fn, cls, *args, **kwargs):
		timer = DurationTimer()
		t = Timer()
		t.start()
		res = fn(cls, *args, **kwargs)
		t.end()
		timer.add(self.name, t)
		if self.callback: self.callback(self.name, t.duration)
		return res

	def __call_property__(self, fn:property, instance):
		timer = DurationTimer()
		t = Timer()
		t.start()
		res = fn.fget(instance)
		t.end()
		timer.add(self.name, t)
		if self.callback: self.callback(self.name, t.duration)
		return res
	
	def __call_method__(self, fn, instance, *args, **kwargs):
		timer = DurationTimer()
		t = Timer()
		t.start()
		res = fn(instance, *args, **kwargs)
		t.end()
		timer.add(self.name, t)
		if self.callback: self.callback(self.name, t.duration)
		return res

