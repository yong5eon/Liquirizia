# -*- coding: utf-8 -*-

import traceback

__all__ = (
	'Error'
)


class Error(BaseException):
	"""
	Error for File Object
	"""
	def __init__(self, reason, error=None):
		if error:
			reason += '\n'
			reason += str(error) + '\n'
			for line in ''.join(traceback.format_tb(error.__traceback__)).strip().split('\n'):
				reason += line + '\n'
		super(Error, self).__init__(reason)
		return
