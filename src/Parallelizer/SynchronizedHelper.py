# -*- coding: utf-8 -*-

__all__ = (
	'SynchronizedHelper'
)


class SynchronizedHelper(object):
	def __init__(self, lock):
		self.lock = lock
		if not self.lock.acquire():
			raise RuntimeError('SynchronizedHelper is not locked.')
		return

	def __del__(self):
		self.lock.release()
		return
