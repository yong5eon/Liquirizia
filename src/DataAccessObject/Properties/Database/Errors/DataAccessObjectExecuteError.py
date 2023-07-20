# -*- coding: utf-8 -*-

from ....DataAccessObjectError import DataAccessObjectError

import traceback

__all__ = (
	'DataAccessObjectExecuteError'
)


class DataAccessObjectExecuteError(DataAccessObjectError):
	"""
	Execute Error Class for Database Access Object
	"""
	def __init__(self, reason=None, sql=None, code=None, error=None):
		if not reason:
			reason = 'Execution is error'
		super(DataAccessObjectExecuteError, self).__init__(reason, error)
		self.sql = sql
		self.code = code
		return

	def __str__(self):
		reason = super(DataAccessObjectExecuteError, self).__str__()
		if self.code:
			reason += self.code + '\n'
		if self.sql:
			reason += self.sql + '\n'
		return reason
