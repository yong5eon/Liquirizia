# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'UnauthorizedError'
)


class UnauthorizedError(Error):
	"""
	Unauthorized Error Class, 401
	"""
	def __init__(self, reason=None, error=None):
		super(UnauthorizedError, self).__init__(401, 'Unauthorized', reason, error)
		return
