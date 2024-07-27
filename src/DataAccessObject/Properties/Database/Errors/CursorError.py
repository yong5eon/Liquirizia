# -*- coding: utf-8 -*-

from ....Error import Error

__all__ = (
	'CursorError'
)


class CursorError(Error):
	"""
	Cursor Error Class for Database Access Object
	"""
	def __init__(self, reason=None, error=None):
		if not reason:
			reason = 'Cursor is error'
		super(Error, self).__init__(reason, error)
		return
