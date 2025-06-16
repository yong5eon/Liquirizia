# -*- coding: utf-8 -*-

from ...Configuration import Configuration as BaseConfiguration

__all__ = (
	'Configuration'
)


class Configuration(BaseConfiguration):
	"""File System Object Configuration Class for Common File System"""

	def __init__(self, path):
		self.base = path
		return
