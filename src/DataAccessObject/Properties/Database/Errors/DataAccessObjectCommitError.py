# -*- coding: utf-8 -*-

from ....DataAccessObjectError import DataAccessObjectError

__all__ = (
	'DataAccessObjectCommitError'
)


class DataAccessObjectCommitError(DataAccessObjectError):
	"""
	Commit Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Transaction is not committed'
		super(DataAccessObjectError, self).__init__(reason, error)
		return
