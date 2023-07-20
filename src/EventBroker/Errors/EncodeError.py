# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'EncodeError'
)


class EncodeError(Error):
	"""
	Encode Error of Event Broker
	"""
	def __init__(self, src, format, charset=None):
		super(EncodeError, self).__init__('Encode Error({}, {}{})'.format(
			src,
			format,
			', {}'.format(charset) if charset else ''
		))
		return
