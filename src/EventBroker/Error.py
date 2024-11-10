# -*- coding: utf-8 -*-

import traceback

__all__ = (
	'Error'
)


class Error(BaseException):
	"""Error Class for Event Broker"""

	def __init__(self, reason, error=None):
		super(Error, self).__init__(reason)
		self.error = error
		return
	
	@property
	def __traceback__(self):
		if self.error:
			return self.error.__traceback__
		return super(Error, self).__traceback__
