# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ConnectionError'
)


class ConnectionError(Error):
	"""Connection Error Class"""

	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Connection is error'
		super(Error, self).__init__(reason, error)
		return
