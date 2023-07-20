# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotSupportedBrokerError'
)


class NotSupportedBrokerError(Error):
	"""
	Not Supported Broker Error Class for Broker Worker
	"""
	def __init__(self, broker):
		super(NotSupportedBrokerError, self).__init__('Not Supported Broker Error({})'.format(broker))
		return
