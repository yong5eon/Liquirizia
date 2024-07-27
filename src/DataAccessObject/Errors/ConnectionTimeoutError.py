# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ConnectionTimeoutError'
)


class ConnectionTimeoutError(Error):
	"""Connection Timeout Error Class"""

	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Connection is timeout'
		super(Error, self).__init__(reason, error)
		return
