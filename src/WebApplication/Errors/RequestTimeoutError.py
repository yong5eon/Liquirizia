# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'RequestTimeoutError'
)


class RequestTimeoutError(Error):
	"""
	Request Timeout Error Class, 408
	"""
	def __init__(self, reason=None, error=None):
		super(RequestTimeoutError, self).__init__(408, 'Request Timeout', reason, error)
		return
