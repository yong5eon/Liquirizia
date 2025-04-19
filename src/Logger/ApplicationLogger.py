# -*- coding: utf-8 -*-

from .Logger import Logger
from .Properties import (
	StreamHandler,
	FileHandler,
	RotateFileHandler,
)
from .Formatters import (
	CommonFormatter,
	ColoredFormatter,
)

from logging import Handler
from uuid import uuid4
from inspect import currentframe
from abc import ABCMeta
from typing import Dict, Any

__all__ = (
	'ApplicationLogger',
)

LOG_FILE_CREATE = 'w'
LOG_FILE_APPEND = 'a'

class ApplicationLoggerCreator(ABCMeta):
	def __call__(cls, *args, **kwargs):
		try:
			o = getattr(cls, '__object__')
			if (len(args) or len(kwargs.items())):
				raise RuntimeError('{} is singleton, it is already initialized'.format(cls.__name__))
			return o
		except AttributeError:
			cls.__object__ = super().__call__(*args, **kwargs)
			return cls.__object__
		

class ApplicationLogger(metaclass=ApplicationLoggerCreator):
	def __init__(self, level: str, handler: Handler = StreamHandler(formatter=ColoredFormatter()), name: str = None):
		self.level = level
		self.logger = Logger(name if name else uuid4().hex)
		self.logger.setLevel(level=level)
		self.logger.addHandler(handler)
		self.loggers = []
		self.handlers = [handler] 
		return
	
	def addLogger(self, name: str):
		logger = Logger(name)
		logger.setLevel(self.level)
		for h in self.handlers:
			logger.addHandler(h)
		self.loggers.append(logger)
		return
	
	def addHandler(self, handler: Handler):
		self.logger.addHandler(handler)
		for logger in self.loggers:
			logger.addHandler(handler)
		self.handlers.append(handler)
		return
	
	def setFile(self, path, mode = LOG_FILE_CREATE, max: int = None, count = 5, formatter=CommonFormatter()):
		h = None
		if max and count:
			h = RotateFileHandler(path, mode, max, count, formatter=formatter)
		else:
			h = FileHandler(path, mode, formatter=formatter)
		if not h:
			return
		self.addHandler(h)	
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
