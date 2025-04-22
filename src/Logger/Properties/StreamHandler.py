# -*- coding: utf-8 -*-

from logging import StreamHandler as BaseStreamHandler

from ..Formatter import Formatter
from ..Formatters import CommonFormatter

from sys import stderr

__all__ = ('StreamHandler')

class StreamHandler(BaseStreamHandler):
	def __init__(self, stream=stderr, formatter: Formatter = CommonFormatter()):
		super().__init__(stream=stream)
		self.formatter = formatter
		return

	def format(self, record):
		return self.formatter(record)
