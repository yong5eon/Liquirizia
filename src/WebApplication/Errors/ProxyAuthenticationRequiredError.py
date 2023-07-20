# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'ProxyAuthenticationRequiredError'
)


class ProxyAuthenticationRequiredError(Error):
	"""
	Proxy Authentication Required Error Class, 407
	"""
	def __init__(self, reason=None, error=None):
		super(ProxyAuthenticationRequiredError, self).__init__(407, 'Proxy Authentication Required', reason, error)
		return
