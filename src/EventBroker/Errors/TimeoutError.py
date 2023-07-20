# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'TimeoutError'
)


class TimeoutError(Error):
	"""
	Timeout Error of Event Broker
	"""
	def __init__(self, reason=None):
		super(TimeoutError, self).__init__('Timeout Error{}'.format('({})'.format(reason) if reason else ''))
		return
