# -*- coding: utf-8 -*-

from ....Error import Error

__all__ = (
	'BeginError'
)


class BeginError(Error):
	"""Begin Error Class"""

	def __init__(self, reason='Tansaction is not began', error=None):
		super(BeginError, self).__init__(reason, error)
		return
