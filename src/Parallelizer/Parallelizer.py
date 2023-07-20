# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .Context import Context
from .Pool import Pool

from .Properties import *

__all__ = (
	'Parallelizer'
)


class Parallelizer(Singleton):
	"""
	Parallelizer for Function
	"""

	def onInit(self, pool=Context.GetThreadPool()):
		self.pool = Pool(pool=pool)
		return

	def __del__(self):
		self.pool.stop()
		return

	@classmethod
	def Run(cls, fn: callable, done: callable=None, error: callable=None, *args, **kwargs):
		inst = cls()
		return inst.run(fn, done, error, *args, **kwargs)

	def run(self, fn: callable, done: callable=None, error: callable=None, *args, **kwargs):
		self.pool.add(Function, fn, done, error, *args, **kwargs)
		return

	@classmethod
	def Stop(cls):
		inst = cls()
		inst.stop()
		return

	def stop(self):
		self.pool.stop()
		return
