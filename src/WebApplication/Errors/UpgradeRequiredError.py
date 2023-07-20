# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'UpgradeRequiredError'
)


class UpgradeRequiredError(Error):
	"""
	Upgrade Required Error Class, 426
	"""
	def __init__(self, reason=None, error=None):
		super(UpgradeRequiredError, self).__init__(426, 'Upgrade Required', reason, error)
		return
