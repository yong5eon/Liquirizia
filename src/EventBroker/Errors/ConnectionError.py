# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ConnectionError'
)


class ConnectionError(Error):
	"""
	Connection Error of Event Broker
	"""
	def __init__(self, reason=None, error=None):
		super(ConnectionError, self).__init__('Connection Error{}'.format('({})'.format(reason) if reason else ''), error)
		return
