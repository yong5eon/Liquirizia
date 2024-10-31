# -*- coding: utf-8 -*-

from ...File import File as IFile
from ...Errors import *

__all__ = (
	'File'
)


class File(IFile):
	"""File Object Class for Common File System"""

	def __init__(self, fso):
		self.fso = fso
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
		if len(path) == 0:
			raise InvalidParametersError('path is not exits')
		if path[0] == '/':
			path = path[1:]
		path = self.fso.conf.base + '/' + path
		try:
			self.fo = open(path, mode, encoding=encoding)
		except FileNotFoundError as e:
			raise NotFoundError('File or Directory is not exist : {}'.format(path), error=e)
		except Exception as e:
			raise e
		return

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

