# -*- coding: utf-8 -*-

from ....Error import Error

import traceback

__all__ = (
	'ExecuteError'
)


class ExecuteError(Error):
	"""Execute Error Class"""

	def __init__(self, reason='Execution is error', error=None, code=None, sql=None, args=None):
		super(ExecuteError, self).__init__(reason, error)
		self.code = code
		self.sql = sql
		self.args = args
		return

	def __str__(self):
		reason = super(ExecuteError, self).__str__()
		if self.code:
			reason += self.code + '\n'
		if self.sql:
			reason += self.sql + '\n'
		if self.args:
			reason += str(self.args)+ '\n'
		return reason
