# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'BadRequestError'
)


class BadRequestError(Error):
	"""
	Bad Request(400) Class
	"""
	def __init__(self, reason=None, error=None):
		super(BadRequestError, self).__init__(400, 'Bad Request', reason, error)
		return
