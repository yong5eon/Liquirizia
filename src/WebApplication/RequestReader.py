# -*- coding: utf-8 -*-

from .Request import Request

from io import BufferedReader

__all__ = (
	'RequestReader'
)


class RequestReader(object):
	"""
	Request Reader Class
	"""
	CRLF = '\r\n'

	def __init__(self, reader: BufferedReader):
		self.reader = reader
		return

	def recv(self, headers: dict = None):
		method, uri, version = self.reqeust()
		h = self.headers()
		for k, v in headers.items() if headers else {}:
			h[k] = v
		return Request(method, uri, version, headers=h)

	def reqeust(self):
		line = self.reader.readline()
		if not line:
			raise ConnectionAbortedError()
		return line.decode().strip(self.__class__.CRLF).split(' ')

	def headers(self):
		headers = {}
		while True:
			header = self.reader.readline().decode().strip(self.__class__.CRLF)
			if not header:
				break
			key, value = header.split(':', 1)
			headers[key.strip()] = value.strip()
		return headers

	def read(self, size=None):
		if size:
			return self.reader.read1(size)
		return self.reader.read()

	def chunk(self):
		line = self.reader.readline()
		size = int(line, 16)
		if not size:
			return None
		buffer = self.reader.read(size)
		self.reader.readline()
		return buffer
