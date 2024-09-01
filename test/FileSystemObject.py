# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.FileSystemObject import (
	FileSystemObjectHelper,
	FileSystemObjectConfiguration,
	FileSystemObject,
	FileObject,
)
from Liquirizia.FileSystemObject.Errors import *
from Liquirizia.FileSystemObject.Errors import FileNotFoundError as FileNotExistError

from os import stat
from os.path import isfile

from time import timezone, mktime
from mimetypes import guess_type
from email.utils import formatdate, parsedate_tz
from hashlib import sha1
from os.path import split


class SampleFileSystemObjectConfiguration(FileSystemObjectConfiguration):
	def __init__(self, path):
		self.base = path
		return
	

class SampleFileSystemObject(FileSystemObject):
	def __init__(self, conf: FileSystemObjectConfiguration):
		self.conf = conf
		return

	def connect(self):
		pass

	def exist(self, path):
		return isfile(self.conf.base + '/' + path)

	def type(self, path):
		return guess_type(self.conf.base + '/' + path)

	def timestamp(self, path):
		stats = stat(self.conf.base + '/' + path)
		if not stats:
			raise RuntimeError('cannot read {} file stats'.format(path))
		try:
			ts = formatdate(stats.st_mtime, usegmt=True)
			return mktime(ts[:8] + (0,)) - (ts[9] or 0) - timezone
		except (TypeError, ValueError, IndexError, OverflowError):
			return None

	def modified(self, path):
		stats = stat(self.conf.base + '/' + path)
		if not stats:
			raise RuntimeError('cannot read {} file stats'.format(path))
		return formatdate(stats.st_mtime, usegmt=True)

	def etag(self, path):
		head, tail = split(self.conf.base + '/' + path)
		stats = stat(self.conf.base + '/' + path)
		if not stats:
			raise RuntimeError('cannot read {} file stats'.format(path))
		etag = '%d:%d:%d:%d:%s'.format(stats.st_dev, stats.st_ino, stats.st_mtime, stats.st_size, tail)
		return sha1(etag.encode('utf-8')).hexdigest()

	def size(self, path):
		stats = stat(self.conf.base + '/' + path)
		if not stats:
			raise RuntimeError('cannot read {} file stats'.format(path))
		return stats.st_size

	def open(self, path, mode='r', encoding=None):
		f = SampleFileObject(self)
		f.open(path, mode)
		return f

	def close(self):
		pass

	def files(self, path):
		pass


class SampleFileObject(FileObject):
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
			raise FileNotExistError('File or Directory is not exist : {}'.format(path), error=e)
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


class TestFileSystemObject(Case):
	@classmethod
	def setUpClass(cls) -> None:
		FileSystemObjectHelper.Set(
			'Sample',
			SampleFileSystemObject,
			SampleFileSystemObjectConfiguration('.')
		)
		return super().setUpClass()
	

	@Parameterized(
			{'v': 'Hello'},
			{'v': 'Hello World'},
			{'v': 'Hello World Yongseon'},
	)
	def testWriteRead(self, v):
		fo = FileSystemObjectHelper.Get('Sample')
		with fo.open('Sample.txt', 'w') as f:
			f.write(v)
			f.close()
		with fo.open('Sample.txt', 'r') as f:
			ASSERT_IS_EQUAL(f.read(), v)
			f.close()
		return
