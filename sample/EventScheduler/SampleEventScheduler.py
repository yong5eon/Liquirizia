# -*- coding: utf-8 -*-

from Liquirizia.EventRunner import EventRunner, EventRunnerProperties
from Liquirizia.EventRunner.Types import EventInterval, EventTimer

from Liquirizia.EventScheduler import EventScheduler

from SampleEventSchedulerHandler import SampleEventSchedulerHandler


class SampleRunner(EventRunner):
	def __init__(self, event: str, headers: dict = None):
		self.event = event
		self.headers = headers
		return

	def run(self, body=None):
		print('EVENT : {} - {} - {}'.format(self.event, self.headers, body))
		return body


if __name__ == '__main__':

	scheduler = EventScheduler('Asia/Seoul', SampleEventSchedulerHandler())
	scheduler.add(EventRunnerProperties(
		SampleRunner,
		type=EventInterval('event.sample.interval', 2000, headers={'c': 3}, body={'a': 2, 'b': 1}),
	))
	scheduler.add(EventRunnerProperties(
		SampleRunner,
		type=EventTimer('event.sample.cron', '*/5 * * * * *', headers={'c': 6}, body={'a': 5, 'b': 4}),
	))
	scheduler.load('*.conf')
	# scheduler.load('.', pattern='*.conf')

	scheduler.run()
