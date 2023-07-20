# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ForbiddenError'
)


class ForbiddenError(Error):
	"""
	Forbidden Error Class, 403
	"""
	def __init__(self, reason=None, error=None):
		super(ForbiddenError, self).__init__(403, 'Forbidden', reason, error)
		return
