# -*- coding: utf-8 -*-

from ..Route import Route
from ..Runnable import Runnable

from Liquirizia.FileSystemObject import FileSystemObject

from Liquirizia.WebApplication import (
	Request,
	RequestFilter,
	ResponseFilter,
	RequestReader,
	ResponseWriter,
	CrossOriginResourceSharing,
)
from Liquirizia.WebApplication.Responses import (
	ResponseBuffer,
	ResponseNotModified,
	ResponseNotFound,
)
from Liquirizia.WebApplication.Util import DateToTimestamp

from re import compile


__all__ = (
	'RunFileSystemObject'
)


class RunFileSystemObject(Route, Runnable):
	"""
	Runner to serve file
	"""

	def __init__(
		self,
		prefix: str,
		fso: FileSystemObject,
		onRequest: RequestFilter = None,
		onRequestOrigin: RequestFilter = None,
		onResponseOrigin: ResponseFilter = None,
		onResponse: ResponseFilter = None,
		cors: CrossOriginResourceSharing = None,
	):
		super(RunFileSystemObject, self).__init__('GET', '{}'.format(prefix), cors=cors)
		self.prefix = prefix
		self.fso = fso
		self.regex = compile('^{}/'.format(prefix))
		self.onRequest = onRequest
		self.onRequestOrigin = onRequestOrigin
		self.onResponseOrigin = onResponseOrigin
		self.onResponse = onResponse
		return

	def match(self, url: str):
		m = self.regex.match(url)
		if not m:
			return False, None
		return True, {
			'path': url[len(self.prefix)+1:]
		}

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

		m, parameters = self.match(request.uri)

		if request.header('ETag') and request.header('ETag') == self.fso.etag(parameters['path']):
			response = ResponseNotModified(version=version)
			writer.send(response, headers=self.headers(request))
			return response

		if request.header('If-Modified-Since'):
			timestamp = DateToTimestamp(request.header('If-Modified-Since'))
			if timestamp and timestamp >= self.fso.timestamp(parameters['path']):
				response = ResponseNotModified(version=version)
				writer.send(response, headers=self.headers(request))
				return response

		# TODO : use cache instead of origin

		if self.onRequestOrigin:
			request, response = self.onRequestOrigin.run(request)
			if response:
				writer.send(response, headers=self.headers(request))
				return response

		m, parameters = self.match(request.uri)

		f = self.fso.open(parameters['path'], mode='rb')

		if not f:
			response = ResponseNotFound()
			writer.send(response, headers=self.headers(request))
			return response

		format, charset = self.fso.type(parameters['path'])

		if request.header('Range'):
			# TODO : seek to range
			pass
		buffer = f.read()

		response = ResponseBuffer(buffer, len(buffer), format=format, charset=charset)

		if self.onResponseOrigin:
			response = self.onResponseOrigin.run(response)

		if self.onResponse:
			response = self.onResponse.run(response)

		writer.send(response, headers=self.headers(request))
		return response
