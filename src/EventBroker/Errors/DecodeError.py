# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'DecodeError'
)


class DecodeError(Error):
	"""
	Decode Error of Event Broker
	"""
	def __init__(self, src, format, charset=None):
		super(DecodeError, self).__init__('Decode Error({}, {}{})'.format(
			src,
			format,
			', {}'.format(charset) if charset else ''
		))
		return
