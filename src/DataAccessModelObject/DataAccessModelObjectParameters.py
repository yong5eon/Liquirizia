# -*- coding: utf-8 -*-

__all__ = (
	'DataAccessModelObjectParameters'
)


class DataAccessModelObjectParameters(object):
	"""
	Data Access Model Object Parameters
	"""
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs
		return
