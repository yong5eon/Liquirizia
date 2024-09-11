# -*- coding: utf-8 -*-

from ....Error import Error

import traceback

__all__ = (
	'ExecuteError'
)


class ExecuteError(Error):
	"""Execute Error Class"""

	def __init__(self, reason='Execution is error', error=None):
		super(ExecuteError, self).__init__(reason, error)
		return
