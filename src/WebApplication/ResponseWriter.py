# -*- coding: utf-8 -*-

from .Response import Response
from .Cookie import Cookie

from http.cookies import SimpleCookie
from io import BufferedWriter

__all__ = (
	'ResponseWriter'
)


class ResponseWriter(object):
	"""
	Response Writer Class
	"""
	CRLF = '\r\n'

	def __init__(self, writer: BufferedWriter, version: str, headers: dict = None):
		self.writer = writer
		self.version = version
		self.headers = headers
		self.cookies = {}
		return

	def send(self, response: Response, headers: dict = None):
		try:
			self.writer.write(str(response).encode())
			self.writer.write(self.__class__.CRLF.encode())
			for key, value in response.headers():
				self.writer.write('{}: {}'.format(key, value).encode())
				self.writer.write(self.__class__.CRLF.encode())
			for k, v in headers.items() if headers else {}:
				self.writer.write('{}: {}{}'.format(k, v, self.__class__.CRLF).encode())
			for k, v in self.headers.items() if self.headers else {}:
				self.writer.write('{}: {}{}'.format(k, v, self.__class__.CRLF).encode())
			self.writer.write(self.__class__.CRLF.encode())
			if response.body:
				self.writer.write(response.body)
		except (ConnectionResetError, ConnectionAbortedError, ConnectionError) as e:
			raise e
		return

	def status(self, status, message):
		self.writer.write('{} {} {}{}'.format(self.version, status, message, self.__class__.CRLF).encode())
		return

	def header(self, key, value):
		self.writer.write('{}: {}{}'.format(key, value, self.__class__.CRLF).encode())
		return

	def cookie(self, name, value, expires=None, path=None, domain=None, secure=None, http=None, version=None, max=None, comment=None):
		self.cookies[name] = Cookie(
			name=name,
			value=value,
			expires=expires,
			path=path,
			domain=domain,
			secure=secure,
			http=http,
			version=version,
			max=max,
			comment=comment
		)
		return

	def begin(self):
		for k, v in self.headers.items() if self.headers else {}:
			self.writer.write('{}: {}{}'.format(k, v, self.__class__.CRLF).encode())

		cookies = SimpleCookie()

		for name, cookie in self.cookies.items():
			cookies[name] = cookie.value
			if cookie.expires:
				cookies[name]['expires'] = cookie.expires
			if cookie.path:
				cookies[name]['path'] = cookie.path
			if cookie.domain:
				cookies[name]['domain'] = cookie.domain
			if cookie.secure:
				cookies[name]['secure'] = cookie.secure
			if cookie.http:
				cookies[name]['httponly'] = cookie.http
			if cookie.version:
				cookies[name]['version'] = cookie.version
			if cookie.max:
				cookies[name]['max-age'] = cookie.max
			if cookie.comment:
				cookies[name]['comment'] = cookie.comment
			self.writer.write('{}: {}{}'.format('Set-Cookie', cookies[name].OutputString(), self.__class__.CRLF).encode())
			self.writer.flush()

		self.writer.write(self.__class__.CRLF.encode())
		self.writer.flush()
		return

	def write(self, buffer):
		self.writer.write(buffer)
		self.writer.flush()
		return

	def chunk(self, buffer=None):
		size = '{:x}'.format(len(buffer) if buffer else 0)
		self.write(size.encode())
		self.write(self.__class__.CRLF.encode())
		if buffer:
			self.write(buffer)
		self.write(self.__class__.CRLF.encode())
		return

	def end(self):
		self.writer.flush()
		self.writer.close()
		return
