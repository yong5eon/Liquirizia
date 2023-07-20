# -*- coding: utf-8 -*-

from Liquirizia.Parallelizer import Handler

import sys

__all__ = (
	'SampleHandler'
)


class SampleHandler(Handler):
	"""
	Runnable Handler Interface for Parallelize
	"""
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
		if error:
			print(str(error), file=sys.stderr)
		return
