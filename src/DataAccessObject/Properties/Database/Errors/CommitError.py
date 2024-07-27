# -*- coding: utf-8 -*-

from ....Error import Error

__all__ = (
	'CommitError'
)


class CommitError(Error):
	"""
	Commit Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Transaction is not committed'
		super(Error, self).__init__(reason, error)
		return
