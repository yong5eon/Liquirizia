# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'InvalidBodyError'
)


class InvalidBodyError(Error):
	"""
	Invalid Body Error for Event Broker
	"""
	def __init__(self, reason=None):
		super(InvalidBodyError, self).__init__('Invalid Body Error{}'.format('({})'.format(reason) if reason else ''))
		return
