# -*- coding: utf-8 -*-

from ..Response import Response
from ..Serializer import SerializerHelper

__all__ = (
	'ResponseRedirect'
)


class ResponseRedirect(Response):
	"""
	HTTP Response Class
	"""
	def __init__(self, url, body=None, format=None, charset=None, version='HTTP/1.1'):
		body = SerializerHelper.Encode(body, format, charset)
		super(ResponseRedirect, self).__init__(
			status=302,
			message='Found',
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
