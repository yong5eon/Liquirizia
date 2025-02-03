# -*- coding: utf-8 -*-

from logging.handlers import RotatingFileHandler as BaseRotateFileHandler

from ..Formatter import Formatter as BaseFormatter
from ..Formatters import Formatter

__all__ = (
	'RotateFileHandledr',
	'LOG_FILE_CREATE',
	'LOG_FILE_APPEND',
)

LOG_FILE_CREATE = 'w'
LOG_FILE_APPEND = 'a'


class RotateFileHandler(BaseRotateFileHandler):
	def __init__(self, filename, mode = LOG_FILE_CREATE, max = 1024 * 1024 * 256, count= 5, formatter: BaseFormatter = Formatter()):
		super().__init__(filename, mode, maxBytes=max, backupCount=count)
		self.formatter = formatter
		return

	def format(self, record):
		try:
			if getattr(record, 'file'):
				record.filename = record.file
			if getattr(record, 'line'):
				record.lineno = record.line
		except AttributeError:
			pass
		return self.formatter(record)

