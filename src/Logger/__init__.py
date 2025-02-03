# -*- coding: utf-8 -*-

from .Logger import Logger
from .ApplicationLogger import ApplicationLogger

from .Properties import StreamHandler
from .Formatter import Formatter
from .Formatters import Formatter as CommonFormatter, ColoredFormatter

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
	'LOG_LEVEL_DEBUG',
	'LOG_LEVEL_INFO',
	'LOG_LEVEL_WARN',
	'LOG_LEVEL_ERROR',
	'LOG_FILE_CREATE',
	'LOG_FILE_APPEND',
	'LOG_FORMAT',
	'LOG_FORMAT_WITH_NAME',
	'LOG_INIT',
	'LOG_SET_FILE',
	'LOG_ADD',
	'LOG_DEBUG',
	'LOG_INFO',
	'LOG_WARN',
	'LOG_ERROR',
)

LOG_LEVEL_DEBUG = 'DEBUG'
LOG_LEVEL_INFO  = 'INFO'
LOG_LEVEL_WARN  = 'WARN'
LOG_LEVEL_ERROR = 'ERROR'

LOG_FILE_CREATE = 'w'
LOG_FILE_APPEND  = 'a'

LOG_FORMAT = '%(asctime)s - %(levelname)-8s - %(process)6d - %(thread)12d - %(fileinfo)-s - %(message)-s'
LOG_FORMAT_WITH_NAME = '%(asctime)s - %(levelname)-8s - %(process)6d - %(thread)12d - %(name)-s - %(fileinfo)-s - %(message)-s'

def LOG_INIT(
	level: str,
	handler: Handler = StreamHandler(formatter=ColoredFormatter(LOG_FORMAT_WITH_NAME)),
):
	_ = ApplicationLogger(level, handler=handler)
	return

def LOG_SET_FILE(
	path: str,
	mode: str = LOG_FILE_CREATE,
	max: int = None,
	count: int = 5,
	formatter: Formatter = CommonFormatter(LOG_FORMAT_WITH_NAME)
):
	_ = ApplicationLogger()
	return _.setFile(path, mode, max, count, formatter=formatter)

def LOG_ADD(name: str):
	_ = ApplicationLogger()
	return _.addLogger(name=name)

def LOG_DEBUG(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = ApplicationLogger()
	return _.debug(msg, e, frame=currentframe().f_back, extra=extra)

def LOG_INFO(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = ApplicationLogger()
	return _.info(msg, e, frame=currentframe().f_back, extra=extra)

def LOG_WARN(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = ApplicationLogger()
	return _.warn(msg, e, frame=currentframe().f_back, extra=extra)

def LOG_ERROR(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = ApplicationLogger()
	return _.error(msg, e, frame=currentframe().f_back, extra=extra)

disable(NOTSET)
captureWarnings(True)