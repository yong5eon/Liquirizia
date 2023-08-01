# -*- coding: utf-8 -*-

from .Error import Error

__all__ = (
	'InvalidParametersError'
)


class InvalidParametersError(Error):
	"""
	Invalid Parameters Error for File Object
	"""
	def __init__(self, reason=None, error=None):
		super(InvalidParametersError, self).__init__('Invalid Parameters Error{}'.format('({})'.format(reason) if reason else None), error if error else self)
		return
