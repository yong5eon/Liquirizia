# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'PreconditionFailedError'
)


class PreconditionFailedError(Error):
	"""
	Precondition Failed Error Class, 412
	"""
	def __init__(self, reason=None, error=None):
		super(PreconditionFailedError, self).__init__(412, 'Precondition Failed', reason, error)
		return
