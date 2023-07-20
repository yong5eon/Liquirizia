# -*- coding: utf-8 -*-

from .Router import Router
from .Properties import (
	RunFile,
	RunFileSystemObject,
	Run,
	RunStream,
	RunWebSocket,
)

from .ServerHandler import ServerHandler
from .RequestHandler import RequestHandler

from Liquirizia.WebApplication import (
	RequestRunnerPropertiesHelper,
	RequestRunner,
	RequestStreamRunner,
	RequestWebSocketRunner,
	RequestFilter,
	ResponseFilter,
	CrossOriginResourceSharing,
)
from Liquirizia.WebApplication.Validator import Validator
from Liquirizia.FileSystemObject import FileSystemObject

from socketserver import ThreadingMixIn, TCPServer
from socket import SOL_SOCKET, SO_REUSEADDR, IPPROTO_TCP, TCP_NODELAY
# from socket import SO_LINGER
# from struct import pack

from platform import system
from os import getcwd, walk
from os.path import splitext, split
from pathlib import Path

__all__ = (
	'Server'
)


class Server(ThreadingMixIn, TCPServer):
	"""
	Web Application Server

	TODO :
	- Serve FileSystemObject
	- Serve Run, RunStream, RunStreamChunked, RunStreamWebSocket
	"""

	INTERVAL = 0.1

	def __init__(
		self,
		host: str = '127.0.0.1',
		port: int = 80,
		version: str = 'HTTP/1.1',
		name: str = None,
		handler: ServerHandler = None,
	):
		super(Server, self).__init__((host, port), RequestHandler)
		self.host = host
		self.port = port
		self.version = version
		self.name = name
		self.handler = handler
		self.router = Router()
		return

	def server_bind(self):
		self.socket.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
		self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		# SO_LINGER
		# 0, 0 -> Close gracefully
		# 1, 0 -> Close immediately
		# 1, Timeout -> Close gracefully with timeout
		#
		# self.socket.setsockopt(SOL_SOCKET, SO_LINGER, pack('ii', 1, 0))
		self.socket.bind(self.server_address)
		return

	def run(self):
		try:
			self.loadRunners()
			if self.handler:
				self.handler.onStart(self.host, self.port, self.version, self.name)
			self.serve_forever(poll_interval=self.__class__.INTERVAL)
		except Exception as e:
			if self.handler:
				self.handler.onError(e)
		finally:
			if self.handler:
				self.handler.onStop()
		return

	def stop(self):
		self.shutdown()
		self.server_close()
		return

	def addFile(
		self,
		path,
		url,
		onRequest: RequestFilter = None,
		onRequestOrigin: RequestFilter = None,
		onResponseOrigin: ResponseFilter = None,
		onResponse: ResponseFilter = None,
	):
		self.router.add(RunFile(
			url,
			path,
			onRequest=onRequest,
			onRequestOrigin=onRequestOrigin,
			onResponseOrigin=onResponseOrigin,
			onResponse=onResponse
		))
		return

	def addFiles(
		self,
		path,
		prefix,
		onRequest: RequestFilter = None,
		onRequestOrigin: RequestFilter = None,
		onResponseOrigin: ResponseFilter = None,
		onResponse: ResponseFilter = None,
	):
		if system().upper() == 'WINDOWS':
			path = getcwd() + '\\' + path.replace('/', '\\')
		else:
			path = getcwd() + '/' + path.replace('\\', '/')

		for (p, dir, files) in walk(path):
			for filename in files:
				ext = splitext(filename)[-1]
				file = ''
				if system().upper() == 'WINDOWS':
					file = '{}\\{}'.format(p, filename)
				else:
					file = '{}/{}'.format(p, filename)
				url = file[len(path):].replace('\\', '/')
				if prefix:
					url = '{}{}'.format(prefix, url)
				self.router.add(RunFile(
					url=url,
					path=file,
					onRequest=onRequest,
					onRequestOrigin=onRequestOrigin,
					onResponseOrigin=onResponseOrigin,
					onResponse=onResponse
				))
		return

	def addFileSystemObject(
		self,
		fso: FileSystemObject,
		prefix,
		onRequest: RequestFilter = None,
		onRequestOrigin: RequestFilter = None,
		onResponseOrigin: ResponseFilter = None,
		onResponse: ResponseFilter = None,
	):
		self.router.add(RunFileSystemObject(
			fso=fso,
			prefix=prefix,
			onRequest=onRequest,
			onRequestOrigin=onRequestOrigin,
			onResponseOrigin=onResponseOrigin,
			onResponse=onResponse
		))
		return

	def add(
		self,
		object: type(RequestRunner),
		method: str,
		url: str,
		qs: Validator = None,
		body: Validator = None,
		onRequest: RequestFilter = None,
		onRequestOrigin: RequestFilter = None,
		onResponseOrigin: ResponseFilter = None,
		onResponse: ResponseFilter = None,
		cors: CrossOriginResourceSharing = None,
	):
		self.router.add(Run(
			object=object,
			method=method,
			url=url,
			qs=qs,
			body=body,
			onRequest=onRequest,
			onRequestOrigin=onRequestOrigin,
			onResponseOrigin=onResponseOrigin,
			onResponse=onResponse,
			cors=cors
		))
		return

	def addStream(
		self,
		object: type(RequestStreamRunner),
		method: str,
		url: str,
		qs: Validator = None,
		cors: CrossOriginResourceSharing = None,
	):
		self.router.add(RunStream(
			object=object,
			method=method,
			url=url,
			qs=qs,
			cors=cors
		))
		return

	def addWebSocket(
		self,
		object: type(RequestWebSocketRunner),
		url: str,
		qs: Validator = None,
		cors: CrossOriginResourceSharing = None,
	):
		self.router.add(RunWebSocket(
			object=object,
			url=url,
			qs=qs,
			cors=cors
		))
		return

	def loadRunners(self):
		for properties in RequestRunnerPropertiesHelper():
			if issubclass(properties['object'], RequestWebSocketRunner):
				self.addWebSocket(
					object=properties['object'],
					url=properties['url'],
					qs=properties['qs'],
					cors=properties['cors'],
				)
			elif issubclass(properties['object'], RequestStreamRunner):
				self.addStream(
					object=properties['object'],
					method=properties['method'],
					url=properties['url'],
					qs=properties['qs'],
					cors=properties['cors'],
				)
			elif issubclass(properties['object'], RequestRunner):
				self.add(
					object=properties['object'],
					method=properties['method'],
					url=properties['url'],
					qs=properties['qs'],
					body=properties['body'],
					onRequest=properties['onRequest'],
					onRequestOrigin=properties['onRequestOrigin'],
					onResponseOrigin=properties['onResponseOrigin'],
					onResponse=properties['onResponse'],
					cors=properties['cors'],
				)
			else:
				raise RuntimeError('{} is not RequestRunner'.format(properties.object.__name__))
		return

	def load(self, path, name='properties', pattern=None):
		if not pattern:
			head, tail = split(path)
			ps = Path(head).glob(tail)
		else:
			ps = Path(path).rglob(pattern)
		for p in ps if ps else []:
			RequestRunnerPropertiesHelper.Add(RequestRunnerPropertiesHelper.Load(str(p), name))
		return
