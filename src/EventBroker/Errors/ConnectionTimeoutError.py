# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ConnectionTimeoutError'
)


class ConnectionTimeoutError(Error):
	"""
	Connection Timeout Error of Event Broker
	"""
	def __init__(self, reason=None, error=None):
		super(ConnectionTimeoutError, self).__init__('Connection Timeout Error{}'.format('({})'.format(reason) if reason else ''), error)
		return
