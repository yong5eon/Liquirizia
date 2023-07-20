# -*- coding: utf-8 -*-

from ..DataAccessObjectError import DataAccessObjectError

__all__ = (
	'DataAccessObjectConnectionTimeoutError'
)


class DataAccessObjectConnectionTimeoutError(DataAccessObjectError):
	"""
	Connection Timeout Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Connection is timeout'
		super(DataAccessObjectError, self).__init__(reason, error)
		return
