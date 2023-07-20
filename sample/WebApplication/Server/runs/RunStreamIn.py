# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import RequestStreamRunner, Request, RequestReader, ResponseWriter
from Liquirizia.WebApplication.Responses import (
	ResponseBadRequest,
	ResponseBuffer,
)

__all__ = (
	'RunStreamIn'
)


class RunStreamIn(RequestStreamRunner):
	def __init__(self, request: Request, parameters):
		self.request = request
		self.parameters = parameters
		return

	def run(self, reader: RequestReader, writer: ResponseWriter):
		if not self.request.size:
			response = ResponseBadRequest('본문의 길이가 없습니다.')
			writer.send(response)
			return response
		data = reader.read(self.request.size)
		response = ResponseBuffer(data, self.request.format, self.request.charset)
		writer.send(response)
		return response
