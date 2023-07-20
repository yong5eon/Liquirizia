# -*- coding: utf-8 -*-

from logging import StreamHandler

__all__ = (
	'Handler',
	'LOG_FILE_APPEND',
	'LOG_FILE_CREATE',
)

LOG_FILE_APPEND = 'a'
LOG_FILE_CREATE = 'w'


class Handler(StreamHandler):
	"""Log Handler Interface"""

	def __init__(self):
		super(Handler, self).__init__()
		return

	def emit(self, record):
		raise RuntimeError('{} have to define handle method to send record'.format(self.__class__.name))
