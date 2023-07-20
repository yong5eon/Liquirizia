# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotPermittedError'
)


class NotPermittedError(Error):
	"""
	Not Permitted Error of Event Broker
	"""
	def __init__(self, reason=None, error=None):
		super(NotPermittedError, self).__init__('Not Permitted Error{}'.format('({})'.format(reason) if reason else ''), error if error else self)
		return
