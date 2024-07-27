# -*- coding: utf-8 -*-

from ....Error import Error

import traceback

__all__ = (
	'ExecuteError'
)


class ExecuteError(Error):
	"""Execute Error Class"""

	def __init__(self, reason='Execution is error', sql=None, code=None, error=None):
		super(ExecuteError, self).__init__(reason, error)
		self.sql = sql
		self.code = code
		return

	def __str__(self):
		reason = super(ExecuteError, self).__str__()
		if self.code:
			reason += self.code + '\n'
		if self.sql:
			reason += self.sql + '\n'
		return reason
