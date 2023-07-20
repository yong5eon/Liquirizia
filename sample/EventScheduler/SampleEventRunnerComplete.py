# -*- coding: utf-8 -*-

from Liquirizia.EventRunner import EventRunnerComplete

__all__ = (
	'SampleEventRunnerComplete'
)


class SampleEventRunnerComplete(EventRunnerComplete):
	def __init__(self, event):
		self.event = event
		return

	def __call__(self, event, headers=None, body=None, res=None):
		print('COMPLETE : {}'.format(event))
		return
