# -*- coding: utf-8 -*-

from .Logger import Logger
from .CommonLogger import CommonLogger
from .Properties import ColoredStreamHandler

from logging import (
	disable, 
	captureWarnings, 
	NOTSET,
	Handler,
)
from inspect import currentframe
from typing import Type, Dict, Any

__all__ = (
	'Logger',
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
	'LOG_EXCEPTION',
)

LOG_LEVEL_DEBUG = 'DEBUG'
LOG_LEVEL_INFO  = 'INFO'
LOG_LEVEL_WARN  = 'WARN'
LOG_LEVEL_ERROR = 'ERROR'

LOG_FILE_CREATE = 'w'
LOG_FILE_APPEND  = 'a'

def LOG_INIT(
	level: str,
	name: str = None,
	format: str = None,
	handler: Handler = ColoredStreamHandler(),
	logger: Type[Logger] = None,
	options: Dict[str, Any] = None
):
	_ = CommonLogger(level, name=name, format=format, handler=handler, logger=logger, options=options)
	return

def LOG_SET_FILE(
	path: str,
	mode: str = LOG_FILE_CREATE,
	max: int = None,
	count: int = 5,
):
	_ = CommonLogger()
	return _.setFile(path, mode, max, count)

def LOG_ADD(name: str):
	_ = CommonLogger()
	return _.add(name=name)

def LOG_DEBUG(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = CommonLogger()
	return _.debug(msg, e, frame=currentframe().f_back, extra=extra)

def LOG_INFO(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = CommonLogger()
	return _.info(msg, e, frame=currentframe().f_back, extra=extra)

def LOG_WARN(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = CommonLogger()
	return _.warn(msg, e, frame=currentframe().f_back, extra=extra)

def LOG_ERROR(msg: str, e: BaseException = None, extra: Dict[str, Any] = None):
	_ = CommonLogger()
	return _.error(msg, e, frame=currentframe().f_back, extra=extra)

def LOG_EXCEPTION(e: BaseException, level: int = LOG_LEVEL_ERROR, extra: Dict[str, Any] = None):
	_ = CommonLogger()
	return _.exception(e, level, frame=currentframe().f_back, extra=extra)

disable(NOTSET)
captureWarnings(True)