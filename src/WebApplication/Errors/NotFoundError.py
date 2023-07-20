# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotFoundError'
)


class NotFoundError(Error):
	"""
	Not Found Error Class, 404
	"""
	def __init__(self, reason=None, error=None):
		super(NotFoundError, self).__init__(404, 'Not Found', reason, error)
		return
