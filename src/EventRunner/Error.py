# -*- coding: utf-8 -*-

import traceback

__all__ = (
	'Error'
)


class Error(BaseException):
	"""
	Error for Event Worker
	"""
	def __init__(self, reason, event=None, body=None, error=None):
		super(Error, self).__init__(reason)
		self.reason = reason
		self.event = event
		self.body = body
		self.error = error
		return

	def __repr__(self):
		return '{}{}{}'.format(
			self.reason,
			' - {}'.format(self.event) if self.event else '',
			' - {}'.format(self.body) if self.body else '',
		)

	def __str__(self):
		reason = '{}{}{}'.format(
			self.reason,
			' - {}'.format(self.event) if self.event else '',
			' - {}'.format(self.body) if self.body else '',
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
