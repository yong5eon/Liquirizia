# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ConnectionClosedError'
)


class ConnectionClosedError(Error):
	"""Connection Closed Error Class"""

	def __init__(self, reason='Connection is closed', error=None):
		super(ConnectionClosedError, self).__init__(reason, error)
		return
