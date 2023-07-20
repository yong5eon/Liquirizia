# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'UnsupportedMediaTypeError'
)


class UnsupportedMediaTypeError(Error):
	"""
	Unsupported Media Type Error Class, 415
	"""
	def __init__(self, reason=None, error=None):
		super(UnsupportedMediaTypeError, self).__init__(415, 'Unsupported Media Type', reason, error)
		return
