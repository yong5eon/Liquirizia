# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import Request
from urllib.parse import urlencode, parse_qs, unquote, parse_qsl, urlparse
from json import loads, JSONDecoder
from datetime import date, datetime


class TypeDecoder(JSONDecoder):
	"""
	Type Decoder for JSON
	"""

	def __init__(self, *args, **kwargs):
		super(TypeDecoder, self).__init__(object_hook=self.any, *args, **kwargs)
		return

	def any(self, obj):
		if isinstance(obj, dict):
			for key, value in obj.items():
				if isinstance(value, str):
					try:
						obj[key] = date.fromisoformat(value)
						continue
					except:
						pass
					try:
						obj[key] = datetime.fromisoformat(value)
						continue
					except:
						pass
				elif isinstance(value, (list, tuple)):
					for i, v in enumerate(value):
						if isinstance(v, str):
							try:
								value[i] = date.fromisoformat(v)
								continue
							except:
								pass
							try:
								value[i] = datetime.fromisoformat(v)
								continue
							except:
								pass
		return obj


if __name__ == '__main__':

	request = Request('GET', '/?a=1&b=2.1&c=안녕&&d=&d=1&d=2&e=', 'HTTP/1.1')
	print(request)
	print(request.qs)
	print(request.body)

	request = Request(
		'GET', '/?a=1&a=2&a=3&b=2.1&b=3&c=안녕&&d={"a": 3, "c": 4}&e=',
		'HTTP/1.1',
		headers={
			'Content-Length': 10
		},
		body='0123456789'.encode('utf-8'),
		format='text/plain',
		charset='utf-8'
	)
	print(request)
	print(request.qs)
	print(request.body)
