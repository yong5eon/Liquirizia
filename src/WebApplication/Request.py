# -*- coding: utf-8 -*-

from .Cookie import Cookie
from .Util import ToHeaderName

from http.cookies import SimpleCookie
from cgi import parse_header
from urllib.parse import parse_qs, unquote, urlencode

__all__ = (
	'Request'
)


class Request(object):
	"""
	HTTP Request Class
	"""
	def __init__(self, method: str, uri: str, version: str, headers: dict = None, body: bytes = None, format: str = None, charset: str = None):
		self.method = method
		# self.uri = uri
		self.path, *querystring = uri.split('?', 1)
		querystring = querystring[0] if len(querystring) else None
		self.args = parse_qs(unquote(querystring), keep_blank_values=True) if querystring else {}
		for k, v in self.args.items():
			if len(v) == 0:
				self.args[k] = None
			elif len(v) == 1:
				self.args[k] = v[0] if len(v[0]) else None
			else:
				for i, o in enumerate(v):
					v[i] = o if len(o) else None
				self.args[k] = v
		self.version = version
		self.props = {}
		self.cookies = {}
		for k, v in headers.items() if headers else []:
			self.header(k, v)
		if body:
			self.header(
				'Content-Type',
				'{}{}'.format(
					format if format else 'application/octet-stream',
					', charset={}'.format(charset) if charset else ''
				)
			)
		self.obj = body
		return

	def __repr__(self):
		return '{} {} {}{}'.format(
			self.method,
			self.path,
			self.version,
			' - {}'.format(self.size) if self.size else '',
		)

	def header(self, key: str, value=None):
		if value:
			if ToHeaderName(key) == 'Cookie':
				c = SimpleCookie()
				c.load(value)
				for k, v in c.items():
					self.cookies[k] = Cookie(
						name=k,
						value=v.value,
						expires=v['expires'],
						path=v['path'],
						domain=v['domain'],
						secure=v['secure'],
						http=v['httponly'],
						version=v['version'],
						max=v['max-age'],
						comment=v['comment']
					)
			else:
				# TODO : according to value, use other parse methods. User-Agent, Accept-Language, ...
				args, kwargs = parse_header(str(value))
				self.props[ToHeaderName(key)] = {
					'expr': str(value),
					'args': args.split(','),
					'kwargs': kwargs
				}
			return
		else:
			if key not in self.props.keys():
				return None
			return self.props[key]['expr']

	def headers(self):
		headers = [(key, value['expr']) for key, value in self.props.items()]

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

		for name, cookie in cookies.items():
			headers.append(('Cookie', cookie.OutputString()))

		return headers

	@property
	def uri(self):
		return '{}{}'.format(
			self.path,
			'?{}'.format(self.querystring) if self.querystring and len(self.querystring) else '',
		)

	@property
	def querystring(self):
		if self.args and len(self.args.items()):
			return urlencode(self.args)
		return None

	@property
	def size(self):
		if 'Content-Length' not in self.props.keys():
			return None
		return int(self.props['Content-Length']['args'][0])

	@property
	def format(self):
		if 'Content-Type' not in self.props.keys():
			return None
		return self.props['Content-Type']['args'][0]

	@property
	def charset(self):
		if 'Content-Type' not in self.props.keys():
			return None
		if 'charset' not in self.props['Content-Type']['kwargs'].keys():
			return None
		return self.props['Content-Type']['kwargs']['charset']

	@property
	def remote(self):
		if 'X-Forwarded-For' in self.props.keys():
			return self.props['X-Forwarded-For']['expr']
		if 'X-Real-IP' in self.props.keys():
			return self.props['X-Real-IP']['expr']
		return self.props['Remote-Address']['expr']

	@property
	def scheme(self):
		if 'X-Forwarded-Proto' in self.props.keys():
			return self.props['X-Forwarded-Proto']['expr']
		return 'HTTP'

	@property
	def qs(self):
		return self.args

	@qs.setter
	def qs(self, args):
		if not isinstance(args, dict):
			raise RuntimeError('querystring must be dict')
		self.args = args
		return

	@property
	def body(self):
		return self.obj

	@body.setter
	def body(self, body):
		self.obj = body
		return
