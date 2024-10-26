# -*- coding: utf-8 -*-

from logging import (
	StreamHandler, 
	Formatter,
	DEBUG,
	INFO,
	WARN,
	ERROR,
)

__all__ = ('ColoredStreamHandler')

BLACK   = '\033[90m'
RED	 = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE	= '\033[94m'
MAGENTA = '\033[95m'
CYAN	= '\033[96m'
WHITE   = '\033[97m'
RESET   = '\033[0m'

class ColoredStreamHandler(StreamHandler):
	def format(self, record):
		try:
			if getattr(record, 'file'):
				record.filename = record.file
			if getattr(record, 'line'):
				record.lineno = record.line
		except AttributeError:
			pass
		formatter = Formatter({
			DEBUG: BLACK  + self.formatter._fmt + RESET,
			INFO : WHITE  + self.formatter._fmt + RESET,
			WARN : YELLOW   + self.formatter._fmt + RESET,
			ERROR: RED	+ self.formatter._fmt + RESET,
		}.get(record.levelno, self.formatter._fmt))
		return formatter.format(record)
