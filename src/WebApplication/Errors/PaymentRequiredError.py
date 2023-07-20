# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'PaymentRequiredError'
)


class PaymentRequiredError(Error):
	"""
	PaymentRequired Error Class, 402
	"""
	def __init__(self, reason=None, error=None):
		super(PaymentRequiredError, self).__init__(402, 'Payment Required', reason, error)
		return
