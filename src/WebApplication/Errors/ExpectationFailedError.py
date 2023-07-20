# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ExpectationFailedError'
)


class ExpectationFailedError(Error):
	"""
	Expectation Failed Error Class, 417
	"""
	def __init__(self, reason=None, error=None):
		super(ExpectationFailedError, self).__init__(417, 'Expectation Failed', reason, error)
		return
