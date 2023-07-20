# -*- coding: utf-8 -*-

from logging import Formatter
from logging.handlers import QueueListener as QueueReceiverBase
from socket import error as socketerror
from errno import EPIPE

__all__ = (
	'QueueReceiver'
)


class QueueReceiver(QueueReceiverBase):
	def __init__(self, queue, handler):
		super(QueueReceiver, self).__init__(queue, handler)
		self.queue=queue
		self.formatter=Formatter('%(asctime)s - %(process)6d - %(thread)6d - %(levelname)-8s - %(message)s')
		return

	def handle(self, record):
		self.callback(record)
		return

	def flush(self, timeout=None):
		try:
			while not self.queue.empty():
				record=self.queue.get(timeout=timeout)
				if not record:
					break
				self.callback(record)
		except socketerror as e:  # socket Error
			pass
		except EOFError as e:
			pass
		except KeyboardInterrupt as e:
			pass
		except IOError as e:
			if e.errno == EPIPE:  # broken pipe
				pass
			else:  # others
				raise e
		except Exception as e:
			raise e
		return

	def stop(self):
		try:
			super(QueueReceiver, self).stop()
		except socketerror as e:  # socket Error
			pass
		except EOFError as e:
			pass
		except KeyboardInterrupt as e:
			pass
		except IOError as e: 
			if e.errno == EPIPE:  # broken pipe
				pass
			else:  # others
				raise e
		except Exception as e:
			raise e
		return

	def format(self, record):
		return self.formatter.format(record)

	def callback(self, record):
		raise RuntimeError('callback must be implemented to handling record of log')
