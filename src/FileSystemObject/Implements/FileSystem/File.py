# -*- coding: utf-8 -*-

from Liquirizia.FileSystemObject import (
	File as BaseFile,
	Connection,
)

__all__ = (
	'File'
)


class File(BaseFile):
	"""File Object Class for Common File System"""

	def __init__(self, fso: Connection):
		self.fso: Connection = fso
		self.fo = None
		return

	def __del__(self):
		if self.fo:
			self.close()
		return

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		return

	def open(self, path, mode='r', encoding=None):
		if path[0] == '/':
			path = path[1:]
		path = self.fso.conf.base + '/' + path
		self.fo = open(path, mode, encoding=encoding)
		return self

	def read(self, size=None):
		return self.fo.read(size if size else -1)

	def write(self, buffer):
		self.fo.write(buffer)
		return

	def close(self):
		if self.fo:
			self.fo.close()
			self.fo = None
		return

