# -*- coding: utf-8 -*-

from ....Error import Error

__all__ = (
	'RollBackError'
)


class RollBackError(Error):
	"""
	Rollback Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Transaction is not rollback'
		super(Error, self).__init__(reason, error)
		return
