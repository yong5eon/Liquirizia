# -*- coding: utf-8 -*-

from logging.handlers import RotatingFileHandler as BaseRotateFileHandler

from ..Formatter import Formatter
from ..Formatters import CommonFormatter

__all__ = (
	'RotateFileHandler',
	'LOG_FILE_CREATE',
	'LOG_FILE_APPEND',
)

LOG_FILE_CREATE = 'w'
LOG_FILE_APPEND = 'a'


class RotateFileHandler(BaseRotateFileHandler):
	def __init__(self, filename, mode = LOG_FILE_CREATE, max = 1024 * 1024 * 256, count= 5, formatter: Formatter = CommonFormatter()):
		super().__init__(filename, mode, maxBytes=max, backupCount=count)
		self.formatter = formatter
		return

	def format(self, record):
		return self.formatter(record)

