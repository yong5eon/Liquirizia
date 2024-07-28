# -*- coding: utf-8 -*-

from ....Error import Error

__all__ = (
	'CursorError'
)


class CursorError(Error):
	"""Cursor Error Class"""

	def __init__(self, reason='Cursor is error', error=None):
		super(CursorError, self).__init__(reason, error)
		return
