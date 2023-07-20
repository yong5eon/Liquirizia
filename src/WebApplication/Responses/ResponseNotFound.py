# -*- coding: utf-8 -*-

from ..Response import Response

from ..Serializer import SerializerHelper

__all__ = (
	'ResponseNotFound'
)


class ResponseNotFound(Response):
	"""
	HTTP Response Class
	"""
	def __init__(self, body=None, format=None, charset=None, version='HTTP/1.1'):
		body = SerializerHelper.Encode(body, format, charset)
		super(ResponseNotFound, self).__init__(
			status=404,
			message='Not Found',
			version=version,
			headers={
				'Content-Length': len(body),
			},
			body=body,
			format=format,
			charset=charset,
		)
		return
