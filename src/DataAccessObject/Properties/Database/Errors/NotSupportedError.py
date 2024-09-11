# -*- coding: utf-8 -*-

from ....Error import Error

__all__ = (
	'NotSupportedError'
)


class NotSupportedError(Error):
	"""Not Supported Error Class"""

	def __init__(self, reason='Operation is not supported', error=None):
		super(NotSupportedError, self).__init__(reason, error)
		return
