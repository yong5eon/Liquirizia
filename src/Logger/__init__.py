# -*- coding: utf-8 -*-

from .Logger import Logger, LOG_LEVEL_DEBUG, LOG_LEVEL_INFO, LOG_LEVEL_WARNING, LOG_LEVEL_ERROR, LOG_LEVEL_CRITICAL, LOG_LEVEL_FATAL
from .Handler import Handler, LOG_FILE_CREATE, LOG_FILE_APPEND
from .Handler import FileHandler, RotateFileHandler, QueueHandler
from .Receiver import QueueReceiver

import traceback

__all__ = (
	'LOG_INITIALIZE',
	'LOG_SET',
	'LOG_SET_FILE',
	'LOG_SET_FILE_ROTATE',
	'LOG_DEBUG',
	'LOG_INFO',
	'LOG_WARNING',
	'LOG_ERROR',
	'LOG_CRITICAL',
	'LOG_FATAL',
	'LOG_EXCEPTION',
	'LOG_LEVEL_DEBUG',
	'LOG_LEVEL_INFO',
	'LOG_LEVEL_WARNING',
	'LOG_LEVEL_ERROR',
	'LOG_LEVEL_CRITICAL',
	'LOG_LEVEL_FATAL',
	'LOG_FILE_APPEND',
	'LOG_FILE_CREATE',
	'Handler',
)


def LOG_INITIALIZE(level=LOG_LEVEL_INFO, format=None, name=None):
	logger = Logger()
	logger.initialize(level, format, name)
	return


def LOG_SET(handler, level=None, formatter=None):
	logger = Logger()
	logger.set(handler, level, formatter)
	return


def LOG_SET_FILE(file, mode=LOG_FILE_CREATE, level=None):
	logger = Logger()
	logger.set(FileHandler(file, mode), level=level)
	return


def LOG_SET_FILE_ROTATE(file, mode=LOG_FILE_CREATE, max=1024 * 1024 * 64, backup=5, level=None):
	logger = Logger()
	logger.set(RotateFileHandler(file, mode, max, backup), level=level)
	return


def LOG_DEBUG(message):
	logger = Logger()
	logger.debug(message)
	return


def LOG_INFO(message):
	logger = Logger()
	logger.info(message)
	return


def LOG_WARNING(message):
	logger = Logger()
	logger.warning(message)
	return


def LOG_ERROR(message):
	logger = Logger()
	logger.error(message)
	return


def LOG_CRITICAL(message):
	logger = Logger()
	logger.critical(message)
	return


def LOG_FATAL(message):
	logger = Logger()
	logger.fatal(message)
	return


def LOG_EXCEPTION(level, e):
	fn = {
		LOG_LEVEL_DEBUG: LOG_DEBUG,
		LOG_LEVEL_INFO: LOG_INFO,
		LOG_LEVEL_WARNING: LOG_WARNING,
		LOG_LEVEL_ERROR: LOG_ERROR,
		LOG_LEVEL_CRITICAL: LOG_CRITICAL,
		LOG_LEVEL_FATAL: LOG_FATAL,
	}.get(level, None)
	if not fn:
		return
	fn(str(e) + '\n' + '\n'.join(traceback.format_tb(e.__traceback__)).strip())
	return
