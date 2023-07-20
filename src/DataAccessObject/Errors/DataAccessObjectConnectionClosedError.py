# -*- coding: utf-8 -*-

from ..DataAccessObjectError import DataAccessObjectError

__all__ = (
	'DataAccessObjectConnectionClosedError'
)


class DataAccessObjectConnectionClosedError(DataAccessObjectError):
	"""
	Connection Closed Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Connection is closed'
		super(DataAccessObjectError, self).__init__(reason, error)
		return
