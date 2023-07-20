# -*- coding: utf-8 -*-

from Liquirizia.EventRunner import EventRunnerError

__all__ = (
	'SampleEventRunnerError'
)


class SampleEventRunnerError(EventRunnerError):
	def __init__(self, event):
		self.event = event
		return

	def __call__(self, event, headers=None, body=None, error=None):
		print('ERROR : {}'.format(event))
		return
