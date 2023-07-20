# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .Context import Context

__all__ = (
	'Proxy'
)


class Proxy(Singleton):
	# TODO : it is possible to use in multi-processing or multi-threading

	def onInit(self):
		self.manager = Context.GetManager()
		return

	@classmethod
	def CreateQueue(cls, size=0):
		proxy = cls()
		return proxy.createQueue(size)

	def createQueue(self, size=0):
		return self.manager.Queue(maxsize=size)

	@classmethod
	def CreateLock(cls):
		proxy = cls()
		return proxy.createLock()

	def createLock(self):
		return self.manager.Lock()

	@classmethod
	def CreateEvent(cls):
		proxy = cls()
		return proxy.createEvent()

	def createEvent(self):
		return self.manager.Event()

	@classmethod
	def CreateCondition(cls, lock=None):
		proxy = cls()
		return proxy.createCondition(lock)

	def createCondition(self, lock=None):
		return self.manager.Condition(lock=lock)

	@classmethod
	def CreateSemaphore(cls, value=1):
		proxy = cls()
		return proxy.createSemaphore(value)

	def createSemaphore(self, value=1):
		return self.manager.Semaphore(value=value)

	@classmethod
	def CreateList(cls, *args, **kwargs):
		proxy = cls()
		return proxy.createList(*args, **kwargs)

	def createList(self, *args, **kwargs):
		return self.manager.list(*args, **kwargs)

	@classmethod
	def CreateDict(cls, *args, **kwargs):
		proxy = cls()
		return proxy.createDict(*args, **kwargs)

	def createDict(self, *args, **kwargs):
		return self.manager.dict(*args, **kwargs)
