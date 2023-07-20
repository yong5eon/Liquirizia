# -*- coding: utf-8 -*-

from Liquirizia.Parallelizer import Handler
from Liquirizia.Parallelizer.MultiThread import Runner

import sys

__all__ = (
	'SampleRunner'
)


class SampleRunner(Runner, Handler):
	def __init__(self):
		super(SampleRunner, self).__init__(self)
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
