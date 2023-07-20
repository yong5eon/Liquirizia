# -*- coding: utf-8 -*-

from ....DataAccessObjectError import DataAccessObjectError

__all__ = (
	'DataAccessObjectNotSupportedError'
)


class DataAccessObjectNotSupportedError(DataAccessObjectError):
	"""
	Not Supported Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Operation is not supported'
		super(DataAccessObjectError, self).__init__(reason, error)
		return
