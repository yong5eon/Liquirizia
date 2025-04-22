# -*- coding: utf-8 -*-

from .Formatter import Formatter

from logging import (
	Formatter as PyFormatter,
	LogRecord,
	DEBUG,
	INFO,
	WARN,
	ERROR,
)

__all__ = (
	'CommonFormatter',
	'ColoredFormatter'
)


BLACK   = '\033[90m'
RED	 = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE	= '\033[94m'
MAGENTA = '\033[95m'
CYAN	= '\033[96m'
WHITE   = '\033[97m'
RESET   = '\033[0m'


class CommonFormatter(Formatter):
	def __init__(self, format: str = None):
		self.formatter = PyFormatter(fmt=format)
		return
	def __call__(self, record: LogRecord):
		try:
			if hasattr(record, 'file'):
				record.filename = record.file
			if hasattr(record, 'line'):
				record.lineno = record.line
			return self.formatter.format(record)
		except Exception as e:
			return PyFormatter().format(record)


class ColoredFormatter(Formatter):
	def __init__(self, format: str = None):
		self.formatter = PyFormatter(fmt=format)
		return
	def __call__(self, record: LogRecord):
		try:
			if hasattr(record, 'file'):
				record.filename = record.file
			if hasattr(record, 'line'):
				record.lineno = record.line
			formatter = PyFormatter({
				DEBUG: BLACK  + self.formatter._fmt + RESET,
				INFO : WHITE  + self.formatter._fmt + RESET,
				WARN : YELLOW + self.formatter._fmt + RESET,
				ERROR: RED	+ self.formatter._fmt + RESET,
			}.get(record.levelno, self.formatter._fmt))
			if record.exc_info:
				record.exc_text = self.formatter.formatException(record.exc_info)
			if record.exc_text:
				record.exc_text = {
					DEBUG: BLACK  + record.exc_text + RESET,
					INFO : WHITE  + record.exc_text + RESET,
					WARN : YELLOW + record.exc_text + RESET,
					ERROR: RED	+ record.exc_text + RESET,
				}.get(record.levelno, record.exc_text)
			return formatter.format(record)
		except Exception as e:
			return PyFormatter().format(record)
