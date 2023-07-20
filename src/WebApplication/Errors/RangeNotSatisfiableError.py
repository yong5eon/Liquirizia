# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'RangeNotSatisfiableError'
)


class RangeNotSatisfiableError(Error):
	"""
	Range Not Satisfiable Error Class, 416
	"""
	def __init__(self, reason=None, error=None):
		super(RangeNotSatisfiableError, self).__init__(416, 'Range Not Satisfiable', reason, error)
		return
