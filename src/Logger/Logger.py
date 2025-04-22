# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from logging import (
	Logger as PyLogger, 
	getLogger,
	Handler,
)
from traceback import format_tb
from inspect import currentframe, getframeinfo
from os.path import basename
from abc import ABCMeta, abstractmethod
from typing import Dict, Any
from uuid import uuid4

__all__ = (
	'Logger',
)


class Logger(Singleton):
	def __init__(
		self,
		level: str,
		name: str = None,
	):
		self.name = name
		self.logger: PyLogger = getLogger(name)
		for h in self.logger.handlers:
			self.logger.removeHandler(h)
		self.logger.setLevel(level)
		self.loggers = []
		self.handlers = []
		return
	
	def get(self, name: str):
		logger: PyLogger = getLogger(name)
		for h in logger.handlers:
			logger.removeHandler(h)
		logger.setLevel(self.logger.level)
		if self.name:
			for h in self.handlers:
				logger.addHandler(h)
		self.loggers.append(logger)
		return self

	def add(self, h: Handler):
		self.logger.addHandler(h)
		if self.name:
			for logger in self.loggers:
				logger.addHandler(h)
		self.handlers.append(h)
		return self
	
	def debug(
		self,
		msg: str,
		e: BaseException = None,
		frame = None,
		extra: Dict[str, Any] = None,
	):
		if not frame: frame = currentframe().f_back
		info = getframeinfo(frame)
		_ = {
			'file': basename(info.filename),
			'line': info.lineno,
		}
		_.update(extra if extra else {})
		return self.logger.debug(
			msg,
			exc_info=e,
			extra=_,
		)

	def info(
		self,
		msg: str,
		e: BaseException = None,
		frame = None,
		extra: Dict[str, Any] = None,
	):
		if not frame: frame = currentframe().f_back
		info = getframeinfo(frame)
		_ = {
			'file': basename(info.filename),
			'line': info.lineno,
		}
		_.update(extra if extra else {})
		return self.logger.info(
			msg,
			exc_info=e,
			extra=_,
		)

	def warn(
		self,
		msg: str,
		e: BaseException = None,
		frame = None,
		extra: Dict[str, Any] = None,
	): 
		if not frame: frame = currentframe().f_back
		info = getframeinfo(frame)
		_ = {
			'file': basename(info.filename),
			'line': info.lineno,
		}
		_.update(extra if extra else {})
		return self.logger.warning(
			msg,
			exc_info=e,
			extra=_,
		)

	def error(
		self,
		msg: str,
		e: BaseException = None,
		frame = None,
		extra: Dict[str, Any] = None,
	):
		if not frame: frame = currentframe().f_back
		info = getframeinfo(frame)
		_ = {
			'file': basename(info.filename),
			'line': info.lineno,
		}
		_.update(extra if extra else {})
		return self.logger.error(
			msg,	
			exc_info=e,
			extra=_,
		)
