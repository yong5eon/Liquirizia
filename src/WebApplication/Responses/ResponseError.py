# -*- coding: utf-8 -*-

from ..Response import Response
from ..Error import Error

from ..Serializer import SerializerHelper

__all__ = (
	'ResponseError'
)


class ResponseError(Response):
	"""
	HTTP Response Class
	"""
	def __init__(self, error: Error, body=None, format=None, charset=None, version='HTTP/1.1'):
		if not body:
			body = SerializerHelper.Encode(str(error), format='text/plain', charset='utf-8')
			super(ResponseError, self).__init__(
				status=error.status,
				message=error.message,
				version=version,
				headers={
					'Content-Length': len(body)
				},
				body=body,
				format='text/plain',
				charset='utf-8'
			)
		else:
			body = SerializerHelper.Encode(body, format=format, charset=charset)
			super(ResponseError, self).__init__(
				status=error.status,
				message=error.message,
				version=version,
				headers={
					'Content-Length': len(body)
				},
				body=body,
				format=format,
				charset=charset
			)
		return
