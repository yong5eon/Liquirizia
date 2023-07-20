# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotImplementedError'
)


class NotImplementedError(Error):
	"""
	Not Implemented Error Class, 501
	"""
	def __init__(self, reason=None, error=None):
		super(NotImplementedError, self).__init__(501, 'Not Implemented', reason, error)
		return
