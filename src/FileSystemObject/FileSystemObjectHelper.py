# -*- coding: utf-8 -*-

from ..Template import Singleton

from .FileSystemObject import FileSystemObject
from .FileSystemObjectConfiguration import FileSystemObjectConfiguration

from .Error import *

__all__ = (
	'FileSystemObjectHelper'
)


class FileSystemObjectHelper(Singleton):
	"""
	File System Object Helper Class

	Sample:
		FileSystemObjectHelper.Set('Sample', YourFileSystemObject, YourFileSystemObjectConfiguration('/path/to'))
		fo = FileSystemObjectHelper.Get('Sample')
		with fo.open('/path/to') as f:
			print(f.read())
			f.close()
	"""
	def onInit(self):
		self.objects = {}
		return

	@classmethod
	def Set(cls, key, o: type(FileSystemObject), conf: FileSystemObjectConfiguration):
		helper = cls()
		return helper.set(key, o, conf)

	def set(self, key, o: type(FileSystemObject), conf: FileSystemObjectConfiguration):
		if not isinstance(o, type):
			raise InvalidParametersError('o is not FileSystemObject')
		self.objects[key] = (o, conf)
		return

	@classmethod
	def Get(cls, key):
		helper = cls()
		return helper.get(key)

	def get(self, key):
		if key not in self.objects:
			return None
		o = self.objects[key][0](self.objects[key][1])
		o.connect()
		return o
