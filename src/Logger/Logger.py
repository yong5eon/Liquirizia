# -*- coding: utf-8 -*-

from ..Template import Singleton
from ..System.Util import GetProcessId, GetHostName

from logging import getLogger, captureWarnings, disable
from logging import Formatter, StreamHandler
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL, FATAL, NOTSET

from .Handler import FileHandler, RotateFileHandler, QueueHandler

__all__ = (
	'Logger',
	'FileHandler',
	'RotateFileHandler',
	'QueueHandler',
	'LOG_LEVEL_DEBUG',
	'LOG_LEVEL_INFO',
	'LOG_LEVEL_WARNING',
	'LOG_LEVEL_ERROR',
	'LOG_LEVEL_CRITICAL',
	'LOG_LEVEL_FATAL',
	'LOG_FILE_APPEND',
	'LOG_FILE_CREATE',
)

LOG_LEVEL_DEBUG = DEBUG
LOG_LEVEL_INFO = INFO
LOG_LEVEL_WARNING = WARNING
LOG_LEVEL_ERROR = ERROR
LOG_LEVEL_CRITICAL = CRITICAL
LOG_LEVEL_FATAL = FATAL

LOG_FILE_APPEND = 'a'
LOG_FILE_CREATE = 'w'


class Logger(Singleton):

	def onInit(self):
		self.logger = None
		self.name = GetHostName()
		self.format = '%(asctime)s - %(process)6d - %(thread)6d - %(levelname)-8s - %(message)s'
		self.formatter = Formatter('%(asctime)s - %(process)6d - %(thread)6d - %(levelname)-8s - %(message)s')
		return

	def initialize(self, level, format=None, name=None):

		disable(NOTSET)

		self.level = level

		if self.level > LOG_LEVEL_ERROR:
			captureWarnings(True)

		if format:
			self.format = format
			self.formatter = Formatter(format)

		# expired to escape tensorflow logs, and set stream Logger as a default Logger
		# basicConfig(format=self.format, level=self.level)

		self.logger = getLogger(name)
		self.logger.setLevel(self.level)

		self.set(StreamHandler())  # set default stream Logger
		return

	def set(self, handler, level=None, formatter=None, format=None):
		if not self.logger:
			self.initialize(LOG_LEVEL_ERROR if not level else level, format='%(message)s')
		handler.setLevel(level if level else self.level)
		handler.setFormatter(self.formatter)
		if formatter:
			handler.setFormatter(formatter)
		if format:
			handler.setFormatter(Formatter(format))
		self.logger.addHandler(handler)
		return

	def debug(self, message):
		if not self.logger:
			self.initialize(LOG_LEVEL_ERROR, format='%(message)s')
		try:
			self.logger.debug(message)
		except (
			BaseException,
			Exception
		) as e:
			pass
		return

	def info(self, message):
		if not self.logger:
			self.initialize(LOG_LEVEL_ERROR, format='%(message)s')
		try:
			self.logger.info(message)
		except (
			BaseException,
			Exception
		) as e:
			pass
		return

	def warning(self, message):
		if not self.logger:
			self.initialize(LOG_LEVEL_ERROR, format='%(message)s')
		try:
			self.logger.warn(message)
		except (
			BaseException,
			Exception
		) as e:
			pass
		return

	def error(self, message):
		if not self.logger:
			self.initialize(LOG_LEVEL_ERROR, format='%(message)s')
		try:
			self.logger.error(message)
		except (
			BaseException,
			Exception
		) as e:
			pass
		return

	def critical(self, message):
		if not self.logger:
			self.initialize(LOG_LEVEL_ERROR, format='%(message)s')
		try:
			self.logger.critical(message)
		except (
			BaseException,
			Exception
		) as e:
			pass
		return

	def fatal(self, message):
		if not self.logger:
			self.initialize(LOG_LEVEL_ERROR, format='%(message)s')
		try:
			self.logger.fatal(message)
		except (
			BaseException,
			Exception
		) as e:
			pass
		return
