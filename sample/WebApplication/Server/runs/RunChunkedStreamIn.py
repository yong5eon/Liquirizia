# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import RequestStreamRunner, Request, RequestReader, ResponseWriter
from Liquirizia.WebApplication.Responses import (
	ResponseBadRequest,
	ResponseBuffer,
)

__all__ = (
	'RunChunkedStreamIn'
)


class RunChunkedStreamIn(RequestStreamRunner):
	def __init__(self, request: Request, parameters: None):
		self.request = request
		self.parameters = parameters
		return

	def run(self, reader: RequestReader, writer: ResponseWriter):
		if not self.request.header('Transfer-Encoding'):
			response = ResponseBadRequest('본문이 청크 형식이 아닙니다.')
			writer.send(response)
			return response
		data = ''
		while 1:
			chunk = reader.chunk()
			if not chunk:
				break
			data += chunk
		response = ResponseBuffer(data, self.request.format, self.request.charset)
		writer.send(response)
		return response
