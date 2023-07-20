# -*- coding: utf-8 -*-

from ..Context import Context
from ..Runner import Runner as RunnerBase

__all__ = (
	'Runner'
)


class Runner(RunnerBase):
	"""
	Multi Thread Runner Class for Parallelize
	"""
	def getPool(self, size):
		return Context.GetThreadPool(size)
