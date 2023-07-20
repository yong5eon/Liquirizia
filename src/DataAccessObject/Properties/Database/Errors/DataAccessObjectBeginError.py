# -*- coding: utf-8 -*-

from ....DataAccessObjectError import DataAccessObjectError

__all__ = (
	'DataAccessObjectBeginError'
)


class DataAccessObjectBeginError(DataAccessObjectError):
	"""
	Begin Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Transaction is not began'
		super(DataAccessObjectError, self).__init__(reason, error)
		return
