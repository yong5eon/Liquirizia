# -*- coding: utf-8 -*-

from ...Configuration import Configuration as IConfiguration

__all__ = (
	'Configuration'
)


class Configuration(IConfiguration):
	"""File System Object Configuration Class for Common File System"""

	def __init__(self, path):
		self.base = path
		return
