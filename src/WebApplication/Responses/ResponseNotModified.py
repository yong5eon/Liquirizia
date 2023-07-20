# -*- coding: utf-8 -*-

from ..Response import Response
from ..Serializer import SerializerHelper

__all__ = (
	'ResponseNotModified'
)


class ResponseNotModified(Response):
	"""
	HTTP Response Not Modified Class
	"""
	def __init__(self, body=None, format=None, charset=None, version='HTTP/1.1'):
		body = SerializerHelper.Encode(body, format, charset)
		super(ResponseNotModified, self).__init__(
			status=304,
			message='Not Modified',
			version=version,
			headers={
				'Content-Length': len(body),
			},
			body=body,
			format=format,
			charset=charset,
		)
		return
