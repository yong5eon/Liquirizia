# -*- coding: utf-8 -*-

__all__ = (
	'EventSchedulerHandler'
)


class EventSchedulerHandler(object):
	"""
	Event Scheduler Handler Interface
	"""
	def onInitialize(self, concurrency):
		raise NotImplementedError('{} must be implemented onInitialize'.format(self.__class__.__name__))

	def onStart(self):
		raise NotImplementedError('{} must be implemented onStart'.format(self.__class__.__name__))

	def onStop(self):
		raise NotImplementedError('{} must be implemented onStop'.format(self.__class__.__name__))

	def onError(self, error=None):
		raise NotImplementedError('{} must be implemented onError'.format(self.__class__.__name__))

	def onInitializeRunner(self, event, headers=None, body=None):
		raise NotImplementedError('{} must be implemented onInitializeConsumer'.format(self.__class__.__name__))

	def onStartRunner(self):
		raise NotImplementedError('{} must be implemented onStartConsumer'.format(self.__class__.__name__))

	def onCompleteRunner(self):
		raise NotImplementedError('{} must be implemented onStartConsumer'.format(self.__class__.__name__))

	def onStopRunner(self):
		raise NotImplementedError('{} must be implemented onStopConsumer'.format(self.__class__.__name__))

	def onErrorRunner(self, error=None):
		raise NotImplementedError('{} must be implemented onErrorConsumer'.format(self.__class__.__name__))

	def onEvent(self, event, headers=None, body=None):
		raise NotImplementedError('{} must be implemented onEvent'.format(self.__class__.__name__))

	def onEventSuccess(self, event, headers=None, body=None, response=None):
		raise NotImplementedError('{} must be implemented onEventSucceeded'.format(self.__class__.__name__))

	def onEventError(self, event, headers=None, body=None, error=None):
		raise NotImplementedError('{} must be implemented onEventError'.format(self.__class__.__name__))
