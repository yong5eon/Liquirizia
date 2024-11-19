# -*- coding: utf-8 -*-

from logging import (
	StreamHandler as BaseStreamHandler, 
)

__all__ = ('StreamHandler')


class StreamHandler(BaseStreamHandler):
	def format(self, record):
		try:
			if getattr(record, 'file'):
				record.filename = record.file
			if getattr(record, 'line'):
				record.lineno = record.line
		except AttributeError:
			pass
		return self.formatter.format(record)
