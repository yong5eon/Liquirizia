# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ConnectionClosed'
)


class ConnectionClosedError(Error):
	"""
	Connection Closed Error of Event Broker
	"""
	def __init__(self, reason=None, error=None):
		super(ConnectionClosedError, self).__init__('Connection is closed{}'.format('({})'.format(reason) if reason else ''), error)
		return
