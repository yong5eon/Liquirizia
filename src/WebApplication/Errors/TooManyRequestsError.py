# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'TooManyRequestsError'
)


class TooManyRequestsError(Error):
	"""
	Too Many Requests Error Class, 429
	"""
	def __init__(self, reason=None, error=None):
		super(TooManyRequestsError, self).__init__(429, 'Too Many Requests', reason, error)
		return
