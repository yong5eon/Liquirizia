# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from multiprocessing import get_context
from multiprocessing.pool import ThreadPool

__all__ = (
	'Context'
)


class Context(Singleton):
	def __init__(self):
		self.context = get_context()
		return

	@classmethod
	def GetManager(cls):
		context = cls()
		return context.getManager()

	def getManager(self):
		return self.context.Manager()

	@classmethod
	def GetProcessPool(cls, concurrency=None):
		context = cls()
		return context.getProcessPool(concurrency=concurrency)

	def getProcessPool(self, concurrency=None):
		try:
			return self.context.Pool(processes=concurrency)
		except Exception as e:
			return None

	@classmethod
	def GetThreadPool(cls, concurrency=None):
		context = cls()
		return context.getThreadPool(concurrency=concurrency)

	def getThreadPool(self, concurrency=None):
		try:
			return ThreadPool(processes=concurrency)
		except Exception as e:
			return None
