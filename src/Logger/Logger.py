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

__all__ = (
	'Logger'
)

LOG_LEVEL_DEBUG = 'DEBUG'
LOG_LEVEL_INFO  = 'INFO'
LOG_LEVEL_WARN  = 'WARN'
LOG_LEVEL_ERROR = 'ERROR'

FORMAT = '%(asctime)s - %(filename)s:%(lineno)d - %(process)6d - %(thread)12d - %(levelname)-8s - %(message)s'
FORMAT_WITH_NAME = '%(asctime)s - %(name)s - %(filename)s(%(lineno)d) - %(process)6d - %(thread)12d - %(levelname)-8s - %(message)s'

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
		self.format = format if format else FORMAT_WITH_NAME if name else FORMAT
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
	
	def debug(self, msg: str, e: BaseException = None, frame = None):
		if not frame: frame = currentframe().f_back
		info = getframeinfo(frame)
		return self.logger.debug(
			'{}{}'.format(msg, '\n{}'.format(self.traceback(e)) if e else ''), 
			extra={
				'file': basename(info.filename),
				'line': info.lineno,
			},
		)

	def info(self, msg: str, e: BaseException = None, frame = None):
		if not frame: frame = currentframe().f_back
		info = getframeinfo(frame)
		return self.logger.info(
			'{}{}'.format(msg, '\n{}'.format(self.traceback(e)) if e else ''), 
			extra={
				'file': basename(info.filename),
				'line': info.lineno,
			},
		)

	def warn(self, msg: str, e: BaseException = None, frame = None): 
		if not frame: frame = currentframe().f_back
		info = getframeinfo(frame)
		return self.logger.warning(
			'{}{}'.format(msg, '\n{}'.format(self.traceback(e)) if e else ''),
			extra={
				'file': basename(info.filename),
				'line': info.lineno,
			},
		)

	def error(self, msg: str, e: BaseException = None, frame = None):
		if not frame: frame = currentframe().f_back
		info = getframeinfo(frame)
		return self.logger.error(
			'{}{}'.format(msg, '\n{}'.format(self.traceback(e)) if e else ''),
			extra={
				'file': basename(info.filename),
				'line': info.lineno,
			},
		)

	def exception(self, e: BaseException, level: str = LOG_LEVEL_ERROR, frame = None):
		if not frame: frame = currentframe().f_back
		reason = '{}\n'.format(str(e))
		for line in ''.join(format_tb(e.__traceback__)).strip().split('\n'):
			reason += line + '\n'
		return {
			DEBUG: self.debug(reason, frame=frame),
			INFO : self.info(reason, frame=frame),
			WARN : self.warn(reason, frame=frame),
			ERROR: self.error(reason, frame=frame),
		}.get(self.value, None)
