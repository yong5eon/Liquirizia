# -*- coding: utf-8 -*-

from ..Response import Response

__all__ = (
	'ResponseBuffer'
)


class ResponseBuffer(Response):
	"""
	HTTP Response Class
	"""

	def __init__(
		self,
		buffer,
		size,
		format,
		charset=None,
		status=200,
		message='OK',
		version='HTTP/1.1'
	):
		super(ResponseBuffer, self).__init__(
			status=status,
			message=message,
			version=version,
			headers={
				'Content-Length': size,
			},
			body=buffer,
			format=format,
			charset=charset
		)
		return
