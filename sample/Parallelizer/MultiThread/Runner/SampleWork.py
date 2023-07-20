# -*- coding: utf-8 -*-

from Liquirizia.Parallelizer import Runnable

from Liquirizia.System.Util import GetProcessId

__all__ = (
	'SampleWork'
)


class SampleWork(Runnable):
	def __init__(self, lck, que):
		super(Runnable, self).__init__()
		self.lock = lck
		self.queue = que
		return

	def run(self):
		while True:
			try:
				self.lock.acquire()
				if self.queue.empty():
					break
				print('{} - {}'.format(GetProcessId(), self.queue.get()))
			finally:
				self.lock.release()
		return
