# -*- coding: utf-8 -*-

from Liquirizia.Parallelizer import Handler
from Liquirizia.Parallelizer.MultiThread import Pool

from .EventSchedulerHandler import EventSchedulerHandler
from .EventContext import EventContext
from .EventRunnerFactory import EventRunnerFactory

__all__ = (
	'EventRunnerPool'
)


class EventRunnerPool(Pool, Handler):
	def __init__(self, context: EventContext, handler: EventSchedulerHandler = None, size: int = None):
		super(EventRunnerPool, self).__init__(size, self)
		self.eventSchedulerHandler = handler
		self.context = context
		return

	def onInitialize(self, *args, **kwargs):
		if self.eventSchedulerHandler:
			self.eventSchedulerHandler.onInitializeRunner(
				args[2],
				args[3],
				args[4],
			)
		return

	def onStart(self):
		if self.eventSchedulerHandler:
			self.eventSchedulerHandler.onStartRunner()
		return

	def onCompleted(self):
		if self.eventSchedulerHandler:
			self.eventSchedulerHandler.onCompleteRunner()
		return

	def onStopped(self):
		if self.eventSchedulerHandler:
			self.eventSchedulerHandler.onStopRunner()
		return

	def onError(self, error=None):
		if self.eventSchedulerHandler:
			self.eventSchedulerHandler.onErrorRunner(error)
		return

	def add(self, event: str, headers: dict = None, body=None):
		p = self.context.match(event)
		super(EventRunnerPool, self).add(
			EventRunnerFactory,
			self.eventSchedulerHandler,
			p,
			event,
			headers,
			body,
		)
		return
