# -*- coding: utf-8 -*-

from ....DataAccessObjectError import DataAccessObjectError

__all__ = (
	'DataAccessObjectRollBackError'
)


class DataAccessObjectRollBackError(DataAccessObjectError):
	"""
	Rollback Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Transaction is not rollback'
		super(DataAccessObjectError, self).__init__(reason, error)
		return
