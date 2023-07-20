# -*- coding: utf-8 -*-

from ..Error import Error

__all__ = (
	'InvalidHeaderError'
)


class InvalidHeaderError(Error):
	"""
	Invalid Header Error for Event Broker
	"""
	def __init__(self, reason=None):
		super(InvalidHeaderError, self).__init__('Invalid Header Error{}'.format('({})'.format(reason) if reason else ''))
		return
