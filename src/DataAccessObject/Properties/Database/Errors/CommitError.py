# -*- coding: utf-8 -*-

from ....Error import Error

__all__ = (
	'CommitError'
)


class CommitError(Error):
	"""Commit Error Class"""
	def __init__(self, reason='Transaction is not committed', error=None):
		super(CommitError, self).__init__(reason, error)
		return
