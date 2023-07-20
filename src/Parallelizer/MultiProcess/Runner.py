# -*- coding: utf-8 -*-

from ..Context import Context
from ..Runner import Runner as RunnerBase

__all__ = (
	'Pool'
)


class Runner(RunnerBase):
	"""
	Multi Process Runner Class for Parallelize
	"""
	def getPool(self, size):
		return Context.GetProcessPool(size)
