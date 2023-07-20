# -*- coding: utf-8 -*-

from ..Runnable import Runnable

__all__ = (
	'Parallelizer'
)


class Function(Runnable):
	def __init__(self, fn: callable, done: callable = None, error: callable = None, *args, **kwargs):
		self.fn = fn
		self.done = done
		self.error = error
		self.args = args
		self.kwargs = kwargs
		return

	def run(self):
		try:
			success = self.fn(*self.args, **self.kwargs)
		except Exception as e:
			if self.error and callable(self.error):
				self.error(error=e)
		else:
			if self.done and callable(self.done):
				self.done(success)
		return
