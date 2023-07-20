# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'URITooLongError'
)


class URITooLongError(Error):
	"""
	URI Too Long Error Class, 414
	"""
	def __init__(self, reason=None, error=None):
		super(URITooLongError, self).__init__(414, 'URI Too Long', reason, error)
		return
