# -*- coding: utf-8 -*-

from ..Response import Response
from ..Serializer import SerializerHelper

__all__ = (
	'ResponseCreated'
)


class ResponseCreated(Response):
	"""
	HTTP Response Class
	"""
	def __init__(self, body=None, format=None, charset=None, version='HTTP/1.1'):
		body = SerializerHelper.Encode(body, format, charset)
		super(ResponseCreated, self).__init__(
			status=201,
			message='Created',
			version=version,
			headers={
				'Content-Length': len(body)
			},
			body=body,
			format=format,
			charset=charset,
		)
		return
