# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.FileSystemObject import (
	Helper,
	Configuration,
	Connection,
	File,
)
from Liquirizia.FileSystemObject.Implements.FileSystem import (
	Configuration as FileSystemConfiguration,
	Connection as FileSystemConnection,
)

from os import stat
from os.path import isfile

from time import timezone, mktime
from mimetypes import guess_type
from email.utils import formatdate, parsedate_tz
from hashlib import sha1
from os.path import split

from random import sample

PATTERN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


class SampleFileSystemObjectConfiguration(Configuration):
	def __init__(self, path):
		self.base = path
		return
	

class SampleFileSystemObject(Connection):
	def __init__(self, conf: SampleFileSystemObjectConfiguration):
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


class SampleFileObject(File):
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
		if path[0] == '/':
			path = path[1:]
		path = self.fso.conf.base + '/' + path
		self.fo = open(path, mode, encoding=encoding)
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
		Helper.Set(
			'Sample',
			SampleFileSystemObject,
			SampleFileSystemObjectConfiguration('.')
		)
		Helper.Set(
			'FileSystem',
			FileSystemConnection,
			FileSystemConfiguration('.')
		)
		return super().setUpClass()

	@Parameterized(
			{'v': 'Hello'},
			{'v': 'Hello World'},
			{'v': 'Hello World Yongseon'},
	)
	def test(self, v):
		fo = Helper.Get('Sample')
		with fo.open('Sample.txt', 'w') as f:
			f.write(v)
			f.close()
		with fo.open('Sample.txt', 'r') as f:
			ASSERT_IS_EQUAL(f.read(), v)
			f.close()
		return
	
	@Parameterized(
			{'v': 'Hello'},
			{'v': 'Hello World'},
			{'v': 'Hello World Yongseon'},
			{'v': 'Hello World Heo Yongseon'},
			{'v': str(sample(PATTERN, 8))},
			{'v': str(sample(PATTERN, 16))},
	)
	def testFileSystem(self, v):
		fo: Connection = Helper.Get('FileSystem')
		with fo.open('Sample.txt', 'w') as f:
			f.write(v)
			f.close()
		with fo.open('Sample.txt', 'r') as f:
			ASSERT_IS_EQUAL(f.read(), v)
			f.close()
		return

