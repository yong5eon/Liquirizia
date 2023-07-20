# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotSupportedError'
)


class NotSupportedError(Error):
	"""
	Not Supported Error of Event Broker
	"""
	def __init__(self, reason=None):
		super(NotSupportedError, self).__init__('Not Supported Error{}'.format(
			'({})'.format(reason) if reason else ''
		))
		return
