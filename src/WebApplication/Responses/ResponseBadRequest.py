# -*- coding: utf-8 -*-

from ..Response import Response

from ..Serializer import SerializerHelper

__all__ = (
	'ResponseBadRequest'
)


class ResponseBadRequest(Response):
	"""
	HTTP Response Class
	"""
	def __init__(self, body=None, format=None, charset=None, version='HTTP/1.1'):
		body = SerializerHelper.Encode(body, format, charset)
		super(ResponseBadRequest, self).__init__(
			status=400,
			message='Bad Request',
			version=version,
			headers={
				'Content-Length': len(body),
			},
			body=body,
			format=format,
			charset=charset,
		)
		return
