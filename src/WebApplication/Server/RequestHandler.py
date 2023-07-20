# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import (
	Request,
	RequestReader,
	Response,
	ResponseWriter,
	Error,
)
from Liquirizia.WebApplication.Responses import (
	ResponseError,
	ResponseOK,
)
from Liquirizia.WebApplication.Errors import (
	InternalServerError,
	MethodNotAllowedError,
	NotFoundError,
	VersionNotSupportedError,
)

from socketserver import StreamRequestHandler

__all__ = (
	'RequestHandler'
)


class RequestHandler(StreamRequestHandler):
	"""
	Request Handler for Web Application Server

	TODO :
	- Set default response for exception
	- Send response instead of exception
	"""

	CRLF = '\r\n'

	def __init__(self, socket, addr, server):
		super(RequestHandler, self).__init__(socket, addr, server)
		self.reader = None
		self.writer = None
		self.address = None
		self.port = None
		self.additionalRequestHeaders = None
		self.additionalResponseHeaders = None
		return

	def setup(self):
		super(RequestHandler, self).setup()
		return

	def handle(self):
		# self.server = server

		# self.writer = ResponseWriter(BufferedWriter(self.wfile))
		self.address = self.client_address[0]
		self.port = self.client_address[1]
		self.additionalRequestHeaders = {
			'Remote-Address': self.client_address[0]
		}
		if self.server.name:
			self.additionalResponseHeaders = {
				'Server': self.server.name
			}
		self.reader = RequestReader(self.rfile)
		self.writer = ResponseWriter(self.wfile, version=self.server.version, headers=self.additionalResponseHeaders)
		request = None
		try:
			if self.server.handler:
				self.server.handler.onConnected(self.address, self.port)
			request = self.reader.recv(headers=self.additionalRequestHeaders)
			if self.server.handler:
				self.server.handler.onRequest(request)
			response = self.run(request)
			if self.server.handler:
				self.server.handler.onRequestSuccess(request, response)
		except Error as e:  # Web Application Error
			if self.server.handler:
				if request:
					self.server.handler.onRequestError(request, e)
				else:
					self.server.handler.onError(e)
			response = ResponseError(e)
			self.writer.send(response, headers=self.additionalResponseHeaders)
			self.connection.close()
		except (ConnectionResetError, ConnectionAbortedError, ConnectionError) as e:
			self.connection.close()
			if self.server.handler:
				self.server.handler.onClosed(self.address, self.port)
		except BaseException as e:
			if self.server.handler:
				self.server.handler.onError(InternalServerError(error=e))
			response = ResponseError(InternalServerError(error=e), version=self.server.version)
			self.writer.send(response, headers=self.additionalResponseHeaders)
			self.connection.close()
		return
	
	def finish(self):
		super(RequestHandler, self).finish()
		return

	def run(self, request: Request):
		if request.version != self.server.version:
			raise VersionNotSupportedError(reason=request.version)

		patterns = self.server.router.matches(request.path)

		if not patterns:
			raise NotFoundError()

		if request.method == 'OPTIONS':
			response = self.options(request, patterns)
			self.writer.send(response)
			return

		if request.method not in patterns.keys():
			raise MethodNotAllowedError()

		runner = patterns[request.method].route
		parameters = patterns[request.method].params

		return runner.run(
			request,
			self.reader,
			self.writer,
			parameters,
			self.server.version,
			self.server.name,
		)

	def options(self, request, patterns):
		if not request.header('Access-Control-Request-Method'):
			response = ResponseOK(
				body=', '.join(patterns.keys()),
				format='text/plain',
				charset='utf-8',
				version=self.server.version
			)
			# response.header('Access-Control-Allow-Methods', ', '.join(patterns.keys()))
			response.header('Allow', ', '.join(patterns.keys()))
			return response

		route = patterns[request.header('Access-Control-Request-Method')].route
		cors = route.headers()

		response = ResponseOK(version=self.server.version)
		for key, value in cors.items():
			response.header(key, value)
		return response
