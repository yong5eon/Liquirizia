# -*- coding: utf-8 -*-

from Liquirizia.WebApplication.Response import Response
from Liquirizia.WebApplication.Util import VersionToString

from Liquirizia.WebApplication.Serializer import SerializerHelper

from http.client import HTTPConnection, HTTPSConnection
from http.cookies import SimpleCookie
from cgi import parse_header

__all__ = (
	'Client'
)


class Client(object):

	def __init__(self, host, port=80, protocol='HTTP', timeout=None):
		connection = {
			'HTTP': HTTPConnection(host=host, port=port, timeout=timeout),
			'HTTPS': HTTPSConnection(host=host, port=port, timeout=timeout),
		}.get(protocol.upper(), None)

		if not connection:
			raise RuntimeError('{} is not support protocol'.format(protocol))

		self.connection = connection
		return

	def __del__(self):
		if self.connection:
			self.close()
		return

	def connect(self):
		try:
			self.connection.connect()
		except Exception as e:
			return False
		return True

	def request(self, method, url, headers={}, buffer=None, size=None, format=None, charset=None):
		try:
			if size:
				headers['Content-Length'] = size
			if format:
				headers['Content-Type'] = '{}{}'.format(format, '; charset={}'.format(charset) if charset else None)
			self.connection.request(
				method,
				url,
				buffer,
				headers
			)
		except Exception as e:
			return False
		return True

	def options(self, url, headers={}):
		return self.request('OPTIONS', url, headers)

	def head(self, url, headers={}):
		return self.request('HEAD', url, headers)

	def get(self, url, headers={}):
		return self.request('GET', url, headers)

	def post(self, url, body, format=None, charset=None, headers={}):
		buffer = SerializerHelper.Encode(body, format, charset)
		return self.request('POST', url, headers, buffer, len(buffer), format, charset)

	def put(self, url, body, format=None, charset=None, headers={}):
		buffer = SerializerHelper.Encode(body, format, charset)
		return self.request('PUT', url, headers, buffer, len(buffer), format, charset)

	def open(self, method, url):
		return self.connection.putrequest(method, url)

	def header(self, key, value):
		return self.connection.putheader(key, value)

	def end(self):
		return self.connection.endheaders()

	def send(self, buffer):
		return self.connection.send(buffer)

	def response(self):
		res = self.connection.getresponse()
		response = Response(
			status=res.status,
			message=res.reason,
			version=VersionToString(res.version)
		)
		for k, v in res.getheaders():
			if k == 'Set-Cookie':
				cookies = SimpleCookie(v)
				for name, cookie in cookies.items():
					response.cookie(
						name,
						cookie.value,
						expires=cookie['expires'] if 'expires' in cookie and cookie['expires'] else None,
						path=cookie['path'] if 'path' in cookie and cookie['path'] else None,
						domain=cookie['domain'] if 'domain' in cookie and cookie['domain'] else None,
						secure=cookie['secure'] if 'secure' in cookie and cookie['secure'] else None,
						http=cookie['httponly'] if 'httponly' in cookie and cookie['httponly'] else None,
						version=cookie['version'] if 'version' in cookie and cookie['version'] else None,
						max=cookie['max-age'] if 'max-age' in cookie and cookie['max-age'] else None,
						comment=cookie['comment'] if 'comment' in cookie and cookie['comment'] else None
					)
			else:
				response.header(k, v)
		
		buffer = res.read()
		if buffer:
			format, props = parse_header(res.getheader('Content-Type'))
			charset = props['charset'] if 'charset' in props else None
			response.body = SerializerHelper.Decode(buffer, format, charset)

		return response

	def close(self):
		self.connection.close()
		return
