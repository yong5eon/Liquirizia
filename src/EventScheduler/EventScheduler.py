# -*- coding: utf-8 -*-

from .EventContext import EventContext
from .EventRunnerPool import EventRunnerPool

from .EventSchedulerHandler import EventSchedulerHandler

from Liquirizia.EventRunner import EventRunnerProperties, EventRunnerPropertiesHelper
from Liquirizia.EventRunner.Types import EventTimer, EventInterval

from apscheduler.schedulers.blocking import BlockingScheduler

from os.path import split
from pathlib import Path

__all__ = (
	'EventScheduler'
)


class EventScheduler(object):
	"""
	EventScheduler
	"""
	def __init__(self, timezone: str, handler: EventSchedulerHandler = None):
		"""
		constructor
		"""
		self.context = EventContext()
		self.scheduler = BlockingScheduler(timezone=timezone)
		self.handler = handler
		self.pool = None
		return

	def run(self, concurrency=None):
		"""
		run as a worker
		"""
		try:
			if self.handler:
				self.handler.onInitialize(concurrency)
			self.pool = EventRunnerPool(self.context, self.handler, size=concurrency)
			for event, properties in self.context.events():
				if isinstance(properties.type, EventTimer):
					self.scheduler.add_job(
						self.callback,
						'cron',
						id=properties.type.event,
						kwargs={'properties': properties},
						second=properties.type.second,
						minute=properties.type.minute,
						hour=properties.type.minute,
						month=properties.type.month,
						day_of_week=properties.type.dayOfWeek,
						year=properties.type.year,
					)
				if isinstance(properties.type, EventInterval):
					self.scheduler.add_job(
						self.callback,
						'interval',
						id=properties.type.event,
						kwargs={'properties': properties},
						seconds=properties.type.interval / 1000,
					)
			if self.handler:
				self.handler.onStart()
			self.scheduler.start()
			if self.handler:
				self.handler.onStop()
		except BaseException as e:
			if self.handler:
				self.handler.onError(e)
		return

	def stop(self):
		self.scheduler.shutdown()
		self.pool.stop()
		return

	def callback(self, properties: EventRunnerProperties):
		self.pool.add(
			properties.type.event,
			properties.type.headers,
			properties.type.body
		)
		return

	def add(self, properties: EventRunnerProperties):
		self.context.add(properties)
		return

	def load(self, path, name='properties', pattern=None):
		if not pattern:
			head, tail = split(path)
			ps = Path(head).glob(tail)
		else:
			ps = Path(path).rglob(pattern)
		for p in ps if ps else []:
			self.add(EventRunnerPropertiesHelper.Load(str(p), name))
		return
