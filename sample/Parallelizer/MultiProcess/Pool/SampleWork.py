# -*- coding: utf-8 -*-

from Liquirizia.Parallelizer import Runnable

from Liquirizia.System.Util import GetProcessId

__all__ = (
	'SampleWork'
)


class SampleWork(Runnable):

	def __init__(self, a, b):
		super(Runnable, self).__init__()
		self.a = a
		self.b = b
		return

	def run(self):
		print('{} - {} + {} = {}'.format(GetProcessId(), self.a, self.b, self.a + self.b))
		return
