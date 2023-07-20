# -*- coding: utf-8 -*-

from ..Context import Context
from ..Pool import Pool as PoolBase
from ..Handler import Handler

__all__ = (
	'Pool'
)


class Pool(PoolBase):
	"""
	Multi Process Pool Class for Parallelize
	"""
	def __init__(self, size=None, handler: Handler = None):
		super(Pool, self).__init__(handler, self.getPool(size))
		return

	def getPool(self, size=None):
		return Context.GetProcessPool(size)
