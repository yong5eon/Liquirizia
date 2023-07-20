# -*- coding: utf-8 -*-

from logging.handlers import RotatingFileHandler as RotateFileHandlerBase

from .Handler import LOG_FILE_CREATE, LOG_FILE_APPEND

__all__ = (
	'RotateFileHandler',
)


class RotateFileHandler(RotateFileHandlerBase):
	"""Rotated File Log Handler"""

	def __init__(self, file, mode=LOG_FILE_CREATE, max=1024 * 1024 * 10, backup=5):
		super(RotateFileHandler, self).__init__(file, mode=mode, maxBytes=max, backupCount=backup)
