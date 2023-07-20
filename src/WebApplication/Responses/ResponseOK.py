# -*- coding: utf-8 -*-

from ..Response import Response
from ..Serializer import SerializerHelper

__all__ = (
	'ResponseOK'
)


class ResponseOK(Response):
	"""
	HTTP Response OK Class
	"""
	def __init__(self, body=None, format=None, charset=None, version='HTTP/1.1'):
		body = SerializerHelper.Encode(body, format, charset)
		super(ResponseOK, self).__init__(
			status=200,
			message='OK',
			version=version,
			headers={
				'Content-Length': len(body)
			},
			body=body,
			format=format,
			charset=charset,
		)
		return
