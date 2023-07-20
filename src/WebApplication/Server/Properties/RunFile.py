# -*- coding: utf-8 -*-

from ..Route import Route
from ..Runnable import Runnable

from Liquirizia.WebApplication import (
	Request,
	RequestFilter,
	ResponseFilter,
	RequestReader,
	ResponseWriter,
	CrossOriginResourceSharing,
)
from Liquirizia.WebApplication.Responses import (
	ResponseFile,
	ResponseNotModified,
)
from Liquirizia.WebApplication.Util import DateToTimestamp, ParseRange

from email.utils import formatdate
from mimetypes import guess_type
from hashlib import sha1
from os import stat
from os.path import split

__all__ = (
	'RunFile'
)


class RunFile(Route, Runnable):
	"""
	Runner to serve file
	"""

	def __init__(
		self,
		url,
		path,
		onRequest: RequestFilter = None,
		onRequestOrigin: RequestFilter = None,
		onResponseOrigin: ResponseFilter = None,
		onResponse: ResponseFilter = None,
		cors: CrossOriginResourceSharing = None,
	):
		super(RunFile, self).__init__('GET', url, cors=cors)
		self.onRequest = onRequest
		self.onRequestOrigin = onRequestOrigin
		self.onResponseOrigin = onResponseOrigin
		self.onResponse = onResponse
		self.path = path
		self.format, self.charset = guess_type(self.path)
		return

	def timestamp(self):
		stats = stat(self.path)
		if not stats:
			raise RuntimeError('cannot read {} file stats'.format(self.path))
		return DateToTimestamp(formatdate(stats.st_mtime, usegmt=True))

	def modified(self):
		stats = stat(self.path)
		if not stats:
			raise RuntimeError('cannot read {} file stats'.format(self.path))
		return formatdate(stats.st_mtime, usegmt=True)

	def etag(self):
		head, tail = split(self.path)
		stats = stat(self.path)
		if not stats:
			raise RuntimeError('cannot read {} file stats'.format(self.path))
		etag = '%d:%d:%d:%d:%s'.format(stats.st_dev, stats.st_ino, stats.st_mtime, stats.st_size, tail)
		return sha1(etag.encode('utf-8')).hexdigest()

	def size(self):
		stats = stat(self.path)
		if not stats:
			raise RuntimeError('cannot read {} file stats'.format(self.path))
		return stats.st_size

	def run(
		self,
		request: Request,
		reader: RequestReader,
		writer: ResponseWriter,
		parameters: dict,
		version: str,
		server: str = None
	):
		if self.onRequest:
			request, response = self.onRequest.run(request)
			if response:
				writer.send(response, headers=self.headers(request))
				return response

		if request.header('ETag') and request.header('ETag') == self.etag():
			response = ResponseNotModified(version=version)
			writer.send(response, headers=self.headers(request))
			return response

		if request.header('If-Modified-Since'):
			timestamp = DateToTimestamp(request.header('If-Modified-Since'))
			if timestamp and timestamp >= self.timestamp():
				response = ResponseNotModified(version=version)
				writer.send(response, headers=self.headers(request))
				return response

		# TODO : do cache instead of origin

		if self.onRequestOrigin:
			request, response = self.onRequestOrigin.run(request)
			if response:
				writer.send(response, headers=self.headers(request))
				return response

		offset, size = None, None
		if request.header('Range'):
			offset, end = ParseRange(request.header('Range'), self.size())
			size = end - offset
		else:
			size = self.size()
		response = ResponseFile(file=self.path, version=version, offset=offset, size=size)

		if self.onResponseOrigin:
			response = self.onResponseOrigin.run(response)

		if self.onResponse:
			response = self.onResponse.run(response)

		writer.send(response, headers=self.headers(request))
		return response
