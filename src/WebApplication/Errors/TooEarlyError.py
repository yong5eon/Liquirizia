# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'TooEarlyError'
)


class TooEarlyError(Error):
	"""
	Too Early Error Class, 425
	"""
	def __init__(self, reason=None, error=None):
		super(TooEarlyError, self).__init__(425, 'Too Early', reason, error)
		return
