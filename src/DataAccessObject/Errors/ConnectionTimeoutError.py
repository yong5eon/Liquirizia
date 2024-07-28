# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ConnectionTimeoutError'
)


class ConnectionTimeoutError(Error):
	"""Connection Timeout Error Class"""

	def __init__(self, reason='Connection is timeout', error=None):
		super(ConnectionTimeoutError, self).__init__(reason, error)
		return
