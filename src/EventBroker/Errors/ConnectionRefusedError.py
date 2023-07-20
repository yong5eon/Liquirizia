# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ConnectionRefusedError'
)


class ConnectionRefusedError(Error):
	"""
	Connection Refused Error of Event Broker
	"""
	def __init__(self, reason=None, error=None):
		super(ConnectionRefusedError, self).__init__('Connection is refused{}'.format('({})'.format(reason) if reason else ''), error)
		return
