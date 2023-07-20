# -*- coding: utf-8 -*-

from ..Response import Response
from ..Serializer import SerializerHelper

__all__ = (
	'ResponseMovePermanently'
)


class ResponseMovePermanently(Response):
	"""
	HTTP Response Move Permanently Class
	"""
	def __init__(self, url, body=None, format=None, charset=None, version='HTTP/1.1'):
		body = SerializerHelper.Encode(body, format, charset)
		super(ResponseMovePermanently, self).__init__(
			status=301,
			message='Move Permanently',
			version=version,
			headers={
				'Content-Length': len(body),
				'Location': url,
			},
			body=body,
			format=format,
			charset=charset,
		)
		return
