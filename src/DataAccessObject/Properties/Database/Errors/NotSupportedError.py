# -*- coding: utf-8 -*-

from ....Error import Error

__all__ = (
	'NotSupportedError'
)


class NotSupportedError(Error):
	"""
	Not Supported Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Operation is not supported'
		super(Error, self).__init__(reason, error)
		return
