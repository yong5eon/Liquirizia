# -*- coding: utf-8 -*-

from .Logger import Logger

from .Properties import StreamHandler, FileHandler, RotateFileHandler
from .Formatter import Formatter, Format
from .Formatters import CommonFormatter, ColoredFormatter

from logging import (
	disable, 
	captureWarnings, 
	NOTSET,
	Handler,
)
from inspect import currentframe
from typing import Dict, Any

__all__ = (
	'Logger',
	'Formatter',
	'Format',
	'LOG_LEVEL_DEBUG',
	'LOG_LEVEL_INFO',
	'LOG_LEVEL_WARN',
	'LOG_LEVEL_ERROR',
	'LOG_FILE_CREATE',
	'LOG_FILE_APPEND',
	'LOG_INIT',
	'LOG_SET_FILE',
	'LOG_ADD',
	'LOG_DEBUG',
	'LOG_INFO',
	'LOG_WARN',
	'LOG_ERROR',
	'LOG_FORMAT',
)

LOG_LEVEL_DEBUG = 'DEBUG'
LOG_LEVEL_INFO  = 'INFO'
LOG_LEVEL_WARN  = 'WARN'
LOG_LEVEL_ERROR = 'ERROR'

LOG_FILE_CREATE = 'w'
LOG_FILE_APPEND  = 'a'

LOG_FORMAT = '%(asctime)s - %(levelname)-8s - %(message)-s'

def LOG_INIT(
	level: str,
	name: str = None,
	handler: Handler = StreamHandler(formatter=ColoredFormatter(LOG_FORMAT)),
):
	_ = Logger(level, name=name)
	_.add(handler)
	return

def LOG_SET_FILE(
	path: str,
	mode: str = LOG_FILE_CREATE,
	max: int = None,
	count: int = 5,
	formatter: Formatter = CommonFormatter(LOG_FORMAT)
):
	_ = Logger()
	h = None
	if max and count:
		h = RotateFileHandler(path, mode, max, count, formatter=formatter)
	else:
		h = FileHandler(path, mode, formatter=formatter)
	if not h:
		return
	return _.add(h)	

def LOG_SET_HANDLER(handler: Handler):
	_ = Logger()
	return _.add(handler)

def LOG_GET(name: str):
	_ = Logger()
	return _.get(name=name)

def LOG_DEBUG(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = Logger()
	return _.debug(msg, e, frame=currentframe().f_back, extra=extra)

def LOG_INFO(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = Logger()
	return _.info(msg, e, frame=currentframe().f_back, extra=extra)

def LOG_WARN(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = Logger()
	return _.warn(msg, e, frame=currentframe().f_back, extra=extra)

def LOG_ERROR(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = Logger()
	return _.error(msg, e, frame=currentframe().f_back, extra=extra)

disable(NOTSET)
captureWarnings(True)