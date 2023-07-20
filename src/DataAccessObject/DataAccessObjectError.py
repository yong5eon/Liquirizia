# -*- coding: utf-8 -*-

import traceback

__all__ = (
	'DataAccessObjectError'
)


class DataAccessObjectError(BaseException):
	"""
	Data Access Object Error Class
	"""
	def __init__(self, reason, error=None):
		super(DataAccessObjectError, self).__init__(reason)
		self.reason = reason
		self.error = error
		return

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		reason = ''
		if self.reason:
			reason += self.reason + '\n'
		if self.error:
			for line in ''.join(traceback.format_tb(self.error.__traceback__)).strip().split('\n'):
				reason += line + '\n'
		else:
			for line in ''.join(traceback.format_tb(self.__traceback__)).strip().split('\n'):
				reason += line + '\n'
		return reason
