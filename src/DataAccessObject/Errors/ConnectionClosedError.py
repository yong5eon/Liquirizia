# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ConnectionClosedError'
)


class ConnectionClosedError(Error):
	"""Connection Closed Error Class"""

	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Connection is closed'
		super(Error, self).__init__(reason, error)
		return
