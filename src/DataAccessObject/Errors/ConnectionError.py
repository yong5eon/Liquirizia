# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ConnectionError'
)


class ConnectionError(Error):
	"""Connection Error Class"""

	def __init__(self, reason='Connection has error', error=None):
		super(ConnectionError, self).__init__(reason, error)
		return
