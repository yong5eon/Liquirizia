# -*- coding: utf-8 -*-

from Liquirizia.Parallelizer import Handler
from Liquirizia.Parallelizer.MultiProcess import Pool

import sys

__all__ = (
	'SamplePool'
)


class SamplePool(Pool, Handler):
	def __init__(self, size=None):
		super(SamplePool, self).__init__(size, self)
		return

	def onInitialize(self, *args, **kwargs):
		print('initialize')
		print(args)
		print(kwargs)
		return

	def onStart(self):
		print('started')
		return

	def onCompleted(self):
		print('completed')
		return

	def onStopped(self):
		print('stopped')
		return

	def onError(self, error=None):
		print('error', file=sys.stderr)
		print(str(error), file=sys.stderr)
		return
