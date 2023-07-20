# -*- coding: utf-8 -*-

from Liquirizia.FileSystemObject.FileSystemObjectConfiguration import FileSystemObjectConfiguration as FileSystemObjectConfigurationBase

__all__ = (
	'FileSystemObjectConfiguration'
)


class FileSystemObjectConfiguration(FileSystemObjectConfigurationBase):
	"""
	File System Object Configuration Class for Common File System
	"""
	def __init__(self, path):
		self.base = path
		return
