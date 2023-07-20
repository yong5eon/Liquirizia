# -*- coding: utf-8 -*-

from ..Response import Response
from ..Serializer import SerializerHelper

__all__ = (
	'ResponseHTML'
)


class ResponseHTML(Response):
	"""
	HTTP Response Class
	"""
	def __init__(self, body, format='text/html', charset='utf-8', status=200, message='OK', version='HTTP/1.1'):
		body = SerializerHelper.Encode(body, format, charset)
		super(ResponseHTML, self).__init__(
			status=status,
			message=message,
			version=version,
			headers={
				'Content-Length': len(body)
			},
			body=body,
			format=format,
			charset=charset,
		)
		return
