# -*- coding: utf-8 -*-

from ..DataAccessObjectError import DataAccessObjectError

__all__ = (
	'DataAccessObjectConnectionError'
)


class DataAccessObjectConnectionError(DataAccessObjectError):
	"""
	Connection Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Connection is error'
		super(DataAccessObjectError, self).__init__(reason, error)
		return
