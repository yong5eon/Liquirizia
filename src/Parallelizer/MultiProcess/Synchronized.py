# -*- coding: utf-8 -*-

from ..Synchronized import Synchronized as SynchronizedBase
from ..SynchronizedHelper import SynchronizedHelper

from multiprocessing import Lock

__all__ = (
	'Synchronized'
)


class Synchronized(SynchronizedBase):
	"""
	Synchronized Interface for Multi Process Parallelize
	"""

	def initialize(self):
		self.lock = Lock()
		return

	def acquire(self):
		if not self.lock.acquire():
			raise RuntimeError('SynchronizedHelper is not locked.')
		return

	def release(self):
		self.lock.release()
		return

	def lock(self):
		return SynchronizedHelper(self.lock)

	def delete(self):
		del self.lock
