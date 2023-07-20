# -*- coding: utf-8 -*-

from .Error import Error

__all__ = (
	'ConnectionClosedError'
)


class ConnectionClosedError(Error):
	"""
	Connection Closed Error for File Object
	"""
	def __init__(self, reason=None, error=None):
		super(ConnectionClosedError, self).__init__('Connection is closed{}'.format('({})'.format(reason) if reason else None), error if error else self)
		return
