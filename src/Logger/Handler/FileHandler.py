# -*- coding: utf-8 -*-

from logging import FileHandler as FileHandlerBase

from .Handler import LOG_FILE_CREATE, LOG_FILE_APPEND

__all__ = (
	'FileHandler'
)


class FileHandler(FileHandlerBase):
	"""File Log Handler"""

	def __init__(self, file, mode=LOG_FILE_CREATE):
		super(FileHandler, self).__init__(file, mode)
		return
