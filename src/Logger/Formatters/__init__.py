# -*- coding: utf-8 -*-

from ..Formatter import Formatter as BaseFormatter

from logging import (
	Formatter as PyLogFormatter,
	LogRecord,
	DEBUG,
	INFO,
	WARN,
	ERROR,
	CRITICAL,
)

__all__ = (
	'Formatter',
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


class Formatter(BaseFormatter):
	def __init__(self, format: str = None):
		self.formatter = PyLogFormatter(fmt=format)
		return
	def __call__(self, record: LogRecord):
		try:
			return self.formatter.format(record)
		except:
			return PyLogFormatter().format(record)


class ColoredFormatter(BaseFormatter):
	def __init__(self, format: str = None):
		self.formatter = PyLogFormatter(fmt=format)
		return
	def __call__(self, record: LogRecord):
		try:
			formatter = PyLogFormatter({
				DEBUG: BLACK  + self.formatter._fmt + RESET,
				INFO : WHITE  + self.formatter._fmt + RESET,
				WARN : YELLOW   + self.formatter._fmt + RESET,
				ERROR: RED	+ self.formatter._fmt + RESET,
				CRITICAL: RED	+ self.formatter._fmt + RESET,
			}.get(record.levelno, self.formatter._fmt))
			return formatter.format(record)
		except:
			return PyLogFormatter().format(record)
