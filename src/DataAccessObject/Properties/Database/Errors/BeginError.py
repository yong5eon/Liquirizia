# -*- coding: utf-8 -*-

from ....Error import Error

__all__ = (
	'BeginError'
)


class BeginError(Error):
	"""
	Begin Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Transaction is not began'
		super(Error, self).__init__(reason, error)
		return
