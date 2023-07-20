# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotAcceptableError'
)


class NotAcceptableError(Error):
	"""
	Not Acceptable Error Class, 406
	"""
	def __init__(self, reason=None, error=None):
		super(NotAcceptableError, self).__init__(406, 'Not Acceptable', reason, error)
		return
