# -*- coding: utf-8 -*-

from .Logger import (
	Logger,
	LOG_LEVEL_DEBUG,
	LOG_LEVEL_INFO,
	LOG_LEVEL_WARN,
	LOG_LEVEL_ERROR,
	LOG_FORMAT,
	LOG_FORMAT_WITH_NAME,
)
from .Properties import (
	ColoredStreamHandler,
	FileHandler,
	RotateFileHandler,
)

from logging import ERROR, Handler
from inspect import currentframe
from abc import ABCMeta

from typing import Type, Dict, Any

__all__ = (
	'CommonLogger',
)

LOG_LEVEL_DEBUG = 'DEBUG'
LOG_LEVEL_INFO  = 'INFO'
LOG_LEVEL_WARN  = 'WARN'
LOG_LEVEL_ERROR = 'ERROR'

LOG_FORMAT = '%(asctime)s - %(fileinfo)-s - %(process)6d - %(thread)12d - %(levelname)-8s - %(message)s'
LOG_FORMAT_WITH_NAME = '%(asctime)s - %(name)s - %(fileinfo)-s - %(process)6d - %(thread)12d - %(levelname)-8s - %(message)s'

LOG_FILE_CREATE = 'w'
LOG_FILE_APPEND = 'a'


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
	def __init__(self, level: str, name: str = None, format: str = None, handler: Handler = ColoredStreamHandler(), logger: Type[Logger] = None, options: Dict[str, Any] = None):
		self.format = format if format else LOG_FORMAT_WITH_NAME if name else LOG_FORMAT
		self.level = level
		self.logger = None
		if logger:
			if not issubclass(logger, Logger):
				raise RuntimeError('{} must be based {}'.format(logger.__name__, Logger.__name__))
			_ = {
				'level': self.level,
				'name': name,
				'format': self.format,
			}
			if options:
				_.update(options)
			self.logger = logger(**_)
		else:
			self.logger = logger if logger else Logger(level, name=name, format=self.format)
		self.handlers: list[Handler] = [handler]
		for h in self.handlers:
			self.logger.add(h)
		self.loggers: list[Logger] = []
		return
	
	def add(self, name: str, level: str = None):
		logger = Logger(level if level else self.level, name, self.format)
		for h in self.handlers:
			logger.add(h)
		self.loggers.append(logger)
		return
	
	def set(self, handler: Handler):
		self.logger.add(handler)
		for logger in self.loggers:
			logger.add(handler)
		self.handlers.append(handler)
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

	def debug(
		self,
		msg: str,
		e: BaseException = None,
		frame = None,
		extra: Dict[str, Any] = None,
	):
		if not frame: frame = currentframe().f_back
		return  self.logger.debug(msg, e, frame=frame, extra=extra)

	def info(
		self,
		msg: str,
		e: BaseException = None,
		frame = None,
		extra: Dict[str, Any] = None,
	):
		if not frame: frame = currentframe().f_back
		return  self.logger.info(msg, e, frame=frame, extra=extra)

	def warn(
		self,
		msg: str,
		e: BaseException = None,
		frame = None,
		extra: Dict[str, Any] = None,
	):
		if not frame: frame = currentframe().f_back
		return  self.logger.warn(msg, e, frame=frame, extra=extra)

	def error(
		self,
		msg: str,
		e: BaseException = None,
		frame = None,
		extra: Dict[str, Any] = None,
	):
		if not frame: frame = currentframe().f_back
		return  self.logger.error(msg, e, frame=frame, extra=extra)

	def exception(
		self,
		e: BaseException,
		level: str = LOG_LEVEL_ERROR,
		frame = None,
		extra: Dict[str, Any] = None,
	):
		if not frame: frame = currentframe().f_back
		return self.logger.exception(e, level=level, frame=frame, extra=extra)
