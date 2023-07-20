# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'NotFoundError'
)


class NotFoundError(Error):
	"""
	Not Found Error of Event Broker
	"""
	def __init__(self, reason=None, error=None):
		super(NotFoundError, self).__init__('Not Found Error{}'.format('({})'.format(reason) if reason else ''), error if error else self)
		return
