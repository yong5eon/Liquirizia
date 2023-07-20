# -*- coding: utf-8 -*-

from multiprocessing import cpu_count as mp_cpu_count
from os import cpu_count as os_cpu_count

__all__ = (
	'GetCPUCount'
)


def GetCPUCount():
	return mp_cpu_count() if mp_cpu_count() else os_cpu_count()
