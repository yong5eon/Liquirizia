# -*- coding: utf-8 -*-

import traceback

__all__ = (
	'Error'
)


class Error(BaseException):
	"""
	Error Class of Web Application
	"""
	def __init__(self, status, message, reason=None, error=None):
		super(Error, self).__init__()
		self.status = status
		self.message = message
		self.reason = reason
		self.error = error
		return

	def __repr__(self):
		return '{} {}{}'.format(
			self.status,
			self.message,
			' - {}'.format(self.reason) if self.reason else ' - {}'.format(str(self.error)) if self.error else '',
		)

	def __str__(self):
		reason = '{} {}{}'.format(
			self.status,
			self.message,
			' - {}'.format(self.reason) if self.reason else ' - {}'.format(str(self.error)) if self.error else '',
		)
		if self.error:
			reason += '\n'
			reason += str(self.error)
			reason += '\n'
			for line in ''.join(traceback.format_tb(self.error.__traceback__)).strip().split('\n'):
				reason += line + '\n'
		else:
			reason += '\n'
			for line in ''.join(traceback.format_tb(self.__traceback__)).strip().split('\n'):
				reason += line + '\n'
		return reason
