# -*- coding: utf-8 -*-

from Liquirizia.Logger import LOG_INITIALIZE, LOG_SET, LOG_SET_FILE, LOG_SET_FILE_ROTATE
from Liquirizia.Logger import LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR, LOG_CRITICAL, LOG_FATAL, LOG_EXCEPTION
from Liquirizia.Logger import LOG_LEVEL_DEBUG, LOG_LEVEL_ERROR

from Liquirizia.Logger import Handler
from Liquirizia.Logger.Handler import QueueHandler
from Liquirizia.Logger.Receiver import QueueReceiver

from Liquirizia.System import Signal

from queue import Queue
from time import sleep


class SampleHandler(Handler):
	def emit(self, record):
		print('Sample Handler - {}'.format(record.message))


class SampleQueueHandler(QueueHandler):
	def __init__(self):
		self.queue = Queue()
		super(SampleQueueHandler, self).__init__(self.queue)
		return


class SampleQueueReceiver(QueueReceiver):
	def __init__(self, handler):
		super(SampleQueueReceiver, self).__init__(handler.queue, handler)
		return

	def callback(self, record):
		print('Sample Queue Receiver - {}'.format(record.message))
		return


if __name__ == '__main__':

	LOG_INITIALIZE(LOG_LEVEL_DEBUG)
	LOG_SET_FILE('Sample.Log')
	LOG_SET_FILE_ROTATE('Sample.Rotate.Log', max=1024, backup=5)
	LOG_SET(SampleHandler())

	LOG_DEBUG('DEBUG')
	LOG_INFO('INFO')
	LOG_WARNING('WARNING')
	LOG_ERROR('ERROR')
	LOG_CRITICAL('CRITICAL')
	LOG_FATAL('FATAL')

	try:
		raise RuntimeError('Sample Runtime Error')
	except RuntimeError as e:
		LOG_EXCEPTION(LOG_LEVEL_ERROR, e)

	h = SampleQueueHandler()
	recv = SampleQueueReceiver(h)

	LOG_SET(h)

	def stop(sig):
		print('flushing...')
		recv.flush()
		print('stopping...')
		recv.stop()
		print('stopped...')
		return

	signal = Signal(Signal.HUP, Signal.INT, Signal.QUIT, Signal.KILL, Signal.STOP, fn=stop)
	signal.attach(Signal.TERM, fn=stop)

	recv.start()

	while not signal.now():
		LOG_DEBUG('SLEEPING IN DEBUG')
		LOG_INFO('SLEEPING IN INFO')
		LOG_WARNING('SLEEPING IN WARNING')
		LOG_ERROR('SLEEPING IN ERROR')
		LOG_CRITICAL('SLEEPING IN CRITICAL')
		LOG_FATAL('SLEEPING IN FATAL')
		sleep(1)
