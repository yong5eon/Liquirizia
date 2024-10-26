# -*- coding: utf-8 -*-

from .Logger import Logger
from .Properties import (
	ColoredStreamHandler,
	FileHandler,
	RotateFileHandler,
)

from logging import ERROR
from inspect import currentframe
from abc import ABCMeta

__all__ = ('CommonLogger')

LOG_LEVEL_DEBUG = 'DEBUG'
LOG_LEVEL_INFO  = 'INFO'
LOG_LEVEL_WARN  = 'WARN'
LOG_LEVEL_ERROR = 'ERROR'

LOG_FILE_CREATE = 'w'
LOG_FILE_APPEND = 'a'

FORMAT = '%(asctime)s - %(filename)s:%(lineno)d - %(process)6d - %(thread)12d - %(levelname)-8s - %(message)s'
FORMAT_WITH_NAME = '%(asctime)s - %(name)s - %(filename)s(%(lineno)d) - %(process)6d - %(thread)12d - %(levelname)-8s - %(message)s'

class Meta(ABCMeta):
	def __call__(cls, *args, **kwargs):
		try:
			o = getattr(cls, '__object__')
			if (len(args) or len(kwargs.items())):
				raise RuntimeError('{} is singleton, it is already initialized'.format(cls.__name__))
			return o
		except AttributeError:
			cls.__object__ = super().__call__(*args, **kwargs)
			return cls.__object__
		

class CommonLogger(metaclass=Meta):
	def __init__(self, level: str, name: str = None, format: str = None):
		self.format = format if format else FORMAT_WITH_NAME if name else FORMAT
		self.logger = Logger(level, name=name, format=self.format)
		self.level = level
		self.handlers = [ColoredStreamHandler()]
		for h in self.handlers:
			self.logger.add(h)
		self.loggers = []
		return
	
	def add(self, name: str, level: str = None):
		logger = Logger(level if level else self.level, name, self.format)
		for h in self.handlers:
			logger.add(h)
		self.loggers.append(logger)
		return

	def setFile(self, path, mode = LOG_FILE_CREATE, max: int = None, count = 5):
		h = None
		if max and count:
			h = RotateFileHandler(path, mode, max, count)
		else:
			h = FileHandler(path, mode)
		if not h:
			return
		self.logger.add(h)
		for logger in self.loggers:
			logger.add(h)
		self.handlers.append(h)
		return

	def debug(self, msg: str, e: BaseException = None, frame = None):
		if not frame: frame = currentframe().f_back
		return  self.logger.debug(msg, e, frame=frame)

	def info(self, msg: str, e: BaseException = None, frame = None):
		if not frame: frame = currentframe().f_back
		return  self.logger.info(msg, e, frame=frame)

	def warn(self, msg: str, e: BaseException = None, frame = None):
		if not frame: frame = currentframe().f_back
		return  self.logger.warn(msg, e, frame=frame)

	def error(self, msg: str, e: BaseException = None, frame = None):
		if not frame: frame = currentframe().f_back
		return  self.logger.error(msg, e, frame=frame)

	def exception(self, e: BaseException, level: str = LOG_LEVEL_ERROR, frame = None):
		if not frame: frame = currentframe().f_back
		return self.logger.exception(e, ERROR, frame=frame)
