# -*- coding: utf-8 -*-

from .Error import Error

__all__ = (
	'FileNotFoundError'
)


class FileNotFoundError(Error):
	"""
	File Not Found Error for File Object
	"""
	def __init__(self, reason=None, error=None):
		super(FileNotFoundError, self).__init__('File Not Found Error{}'.format('({})'.format(reason) if reason else None), error if error else self)
		return
