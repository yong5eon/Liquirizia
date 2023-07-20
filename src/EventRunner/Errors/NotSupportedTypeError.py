# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotSupportedTypeError'
)


class NotSupportedTypeError(Error):
	"""
	Not Supported Type Error Class for Type Worker
	"""
	def __init__(self, type):
		super(NotSupportedTypeError, self).__init__('Not Supported Type Error({})'.format(type))
		return
