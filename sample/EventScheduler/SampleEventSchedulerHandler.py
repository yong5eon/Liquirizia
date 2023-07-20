# -*- coding: utf-8 -*-

from Liquirizia.Logger import LOG_INITIALIZE, LOG_LEVEL_DEBUG, LOG_INFO, LOG_ERROR, LOG_EXCEPTION, LOG_DEBUG

from Liquirizia.EventScheduler import EventSchedulerHandler

__all__ = (
	'SampleEventSchedulerHandler'
)


class SampleEventSchedulerHandler(EventSchedulerHandler):
	def onInitialize(self, concurrency):
		LOG_INITIALIZE(LOG_LEVEL_DEBUG, name='EVENT_WORKER')
		LOG_INFO('EVENT WORKER INIT     : {}'.format(concurrency))
		return

	def onStart(self):
		LOG_INFO('EVENT WORKER START')
		return

	def onStop(self):
		LOG_INFO('EVENT WORKER STOP')
		return

	def onError(self, error=None):
		LOG_ERROR('EVENT WORKER ERROR    :')
		LOG_EXCEPTION(LOG_LEVEL_DEBUG, error)
		return

	def onInitializeRunner(self, event, headers=None, body=None):
		LOG_INFO('EVENT RUNNER INIT     : {}, {}, {}'.format(
			event,
			headers,
			body,
		))
		return

	def onStartRunner(self):
		LOG_INFO('EVENT RUNNER START')
		return

	def onCompleteRunner(self):
		LOG_INFO('EVENT RUNNER COMPLETE')
		return

	def onStopRunner(self):
		LOG_INFO('EVENT RUNNER STOP')
		return

	def onErrorRunner(self, error=None):
		LOG_ERROR('EVENT RUNNER ERROR    : ')
		LOG_EXCEPTION(LOG_LEVEL_DEBUG, error)
		return

	def onEvent(self, event, headers=None, body=None):
		LOG_INFO('EVENT                 : {}, {}, {}'.format(
			event,
			headers,
			body,
		))
		return

	def onEventSuccess(self, event, headers=None, body=None, response=None):
		LOG_INFO('EVENT SUCCESS         : {}, {}, {}, {}'.format(
			event,
			headers,
			body,
			response
		))
		return

	def onEventError(self, event, headers=None, body=None, error=None):
		LOG_ERROR('EVENT ERROR           : {}, {}, {}'.format(
			event,
			headers,
			body,
		))
		if error:
			LOG_EXCEPTION(LOG_LEVEL_DEBUG, error)
		return
