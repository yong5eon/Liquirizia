# -*- coding: utf-8 -*-

from logging import (
	Logger as PyLogger, 
	getLogger,
	Formatter,
	Handler,
	DEBUG,
	INFO,
	WARN,
	ERROR,
)
from traceback import format_tb
from inspect import currentframe, getframeinfo
from os.path import basename

from typing import Dict, Any

__all__ = (
	'Logger',
)

LOG_LEVEL_DEBUG = 'DEBUG'
LOG_LEVEL_INFO  = 'INFO'
LOG_LEVEL_WARN  = 'WARN'
LOG_LEVEL_ERROR = 'ERROR'

LOG_FORMAT = '%(asctime)s - %(fileinfo)-s - %(process)6d - %(thread)12d - %(levelname)-8s - %(message)s'
LOG_FORMAT_WITH_NAME = '%(asctime)s - %(name)s - %(fileinfo)-s - %(process)6d - %(thread)12d - %(levelname)-8s - %(message)s'


class Logger(object):
	def __init__(
		self,
		level: str,
		name: str = None,
		format: str = None,
	):
		self.logger: PyLogger = getLogger(name)
		self.logger.setLevel(level)
		self.level = level
		self.format = format if format else LOG_FORMAT_WITH_NAME if name else LOG_FORMAT
		for h in self.logger.handlers:
			self.logger.removeHandler(h)
		return
	
	def add(self, h: Handler):
		h.setLevel(self.level)
		h.setFormatter(Formatter(self.format))
		self.logger.addHandler(h)
		return
	
	def traceback(self, e: BaseException):
		return ''.join(format_tb(e.__traceback__)).strip()
	
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
			'fileinfo': '{}:{}'.format(basename(info.filename), info.lineno),
		}
		_.update(extra if extra else {})
		return self.logger.debug(
			'{}{}'.format(msg, '\n{}'.format(self.traceback(e)) if e else ''), 
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
			'fileinfo': '{}:{}'.format(basename(info.filename), info.lineno),
		}
		_.update(extra if extra else {})
		return self.logger.info(
			'{}{}'.format(msg, '\n{}'.format(self.traceback(e)) if e else ''), 
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
			'fileinfo': '{}:{}'.format(basename(info.filename), info.lineno),
		}
		_.update(extra if extra else {})
		return self.logger.warning(
			'{}{}'.format(msg, '\n{}'.format(self.traceback(e)) if e else ''),
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
			'fileinfo': '{}:{}'.format(basename(info.filename), info.lineno),
		}
		_.update(extra if extra else {})
		return self.logger.error(
			'{}{}'.format(msg, '\n{}'.format(self.traceback(e)) if e else ''),
			extra=_,
		)

	def exception(
		self,
		e: BaseException,
		level: str = LOG_LEVEL_ERROR,
		frame = None,
		extra: Dict[str, Any] = None,
	):
		if not frame: frame = currentframe().f_back
		info = getframeinfo(frame)
		_ = {
			'file': basename(info.filename),
			'line': info.lineno,
			'fileinfo': '{}:{}'.format(basename(info.filename), info.lineno),
		}
		_.update(extra if extra else {})
		reason = '{}\n'.format(str(e))
		for line in ''.join(format_tb(e.__traceback__)).strip().split('\n'):
			reason += line + '\n'
		return {
			DEBUG: self.debug(reason, frame=frame, extra=extra),
			INFO : self.info(reason, frame=frame, extra=extra),
			WARN : self.warn(reason, frame=frame, extra=extra),
			ERROR: self.error(reason, frame=frame, extra=extra),
		}.get(level, None)
