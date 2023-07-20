# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'InternalServerError'
)


class InternalServerError(Error):
	"""
	Internal Server Error Class, 500
	"""
	def __init__(self, reason=None, error=None):
		super(InternalServerError, self).__init__(500, 'Internal Server Error', reason, error)
		return
