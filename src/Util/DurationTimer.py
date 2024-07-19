# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from time import time
from functools import wraps

__all__ = (
	'DurationTimer',
	'Duration',
)


class Timer(object):
	"""Timer Class"""
	def __init__(self) -> None:
		self.ts = None
		self.te = None
		self.duration = None
		return
	
	def __str__(self):
		return '{:.03f}'.format(self.duration)

	def start(self):
		self.ts = time()
		return self.ts
	def end(self):
		self.te = time()
		self.duration = self.te - self.ts
		return self.te


class DurationTimer(Singleton):
	"""Duration Timer Class"""
	def __init__(self) -> None:
		self.table = {}
		return
	def add(self, name, timer : Timer):
		if name not in self.table.keys():
			self.table[name] = []
		self.table[name].append(timer)
		return
	def min(self, name):
		pass
	def max(self, name):
		pass
	def avg(self, name):
		pass


def Duration(name: str = None):
	def decorator(fn):
		if not callable(fn):
			raise RuntimeError('{} is not callable'.format(fn.__qualname__))
		@wraps(fn)
		def run(*args, **kwargs):
			timer = DurationTimer()
			t = Timer()
			t.start()
			res = fn(*args, **kwargs)
			t.end()
			timer.add(
				name if name else fn.__qualname__,
				t
			)
			return res
		return
	return decorator
