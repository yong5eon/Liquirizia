# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'MethodNotAllowedError'
)


class MethodNotAllowedError(Error):
	"""
	Method Not Allowed Error Class, 405
	"""
	def __init__(self, reason=None, error=None):
		super(MethodNotAllowedError, self).__init__(405, 'Method Not Allowed', reason, error)
		return
