# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotSupportedEventError'
)


class NotSupportedEventError(Error):
	"""
	Not Supported Event Error Class for Event Worker
	"""
	def __init__(self, event):
		super(NotSupportedEventError, self).__init__('Not Supported Event Error({})'.format(event))
		return
