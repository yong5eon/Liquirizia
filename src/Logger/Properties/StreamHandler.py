# -*- coding: utf-8 -*-

from logging import StreamHandler as BaseStreamHandler

from ..Formatter import Formatter as BaseFormatter
from ..Formatters import Formatter

from sys import stderr

__all__ = ('StreamHandler')

class StreamHandler(BaseStreamHandler):
	def __init__(self, stream=stderr, formatter: BaseFormatter = Formatter()):
		super().__init__(stream=stream)
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
