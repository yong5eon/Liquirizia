# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotSupportedTypeError'
)


class NotSupportedTypeError(Error):
	"""
	Not Supported Type Error of Event Broker
	"""
	def __init__(self, format, charset=None):
		super(NotSupportedTypeError, self).__init__('Not Supported Type Error({}{})'.format(
			format,
			', {}'.format(charset) if charset else ''
		))
		return
