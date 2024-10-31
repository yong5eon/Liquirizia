# -*- coding: utf-8 -*-

from ...Connection import Connection as IConnection

from .File import File
from .Configuration import Configuration

from os import stat
from os.path import isfile

from time import timezone, mktime
from mimetypes import guess_type
from email.utils import formatdate, parsedate_tz
from hashlib import sha1
from os.path import split

__all__ = (
	'Connection'
)


class Connection(IConnection):
	"""File Object Class for Common File System"""

	def __init__(self, conf: Configuration):
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
		f = File(self)
		f.open(path, mode)
		return f

	def close(self):
		pass

	def files(self, path):
		pass
