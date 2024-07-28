# -*- coding: utf-8 -*-

from ....Error import Error

__all__ = (
	'RollBackError'
)


class RollBackError(Error):
	"""Rollback Error Class"""

	def __init__(self, reason='Transaction is not rollback', error=None):
		super(RollBackError, self).__init__(reason, error)
		return
