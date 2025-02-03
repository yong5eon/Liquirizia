# -*- coding: utf-8 -*-

from logging import (
	Logger as PyLogger, 
	getLogger,
	Handler,
)
from traceback import format_tb
from inspect import currentframe, getframeinfo
from os.path import basename

from typing import Dict, Any

__all__ = (
	'Logger',
)

class Logger(object):
	def __init__(
		self,
		name: str = None,
	):
		self.logger: PyLogger = getLogger(name)
		for h in self.logger.handlers:
			self.logger.removeHandler(h)
		return
	
	def setLevel(self, level: str):
		self.logger.setLevel(level)
		return
	
	def addHandler(self, h: Handler):
		self.logger.addHandler(h)
		return
	
	def traceback(self, e: BaseException):
		return ''.join(format_tb(e.__traceback__)).strip().replace(' ' * 4, ' ' * 2)
	
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
