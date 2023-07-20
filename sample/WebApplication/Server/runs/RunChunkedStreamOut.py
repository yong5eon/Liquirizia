# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import RequestStreamRunner, Request, RequestReader, ResponseWriter
from Liquirizia.WebApplication.Serializer import SerializerHelper

from time import sleep

__all__ = (
	'RunChunkedStreamOut'
)


class RunChunkedStreamOut(RequestStreamRunner):
	def __init__(self, request: Request, parameters):
		self.request = request
		self.parameters = parameters
		return

	def run(self, reader: RequestReader, writer: ResponseWriter):
		writer.status(200, 'OK')
		writer.header('Transfer-Encoding', 'chunked')
		writer.header('Content-Type', 'text/plain; charset=utf-8')
		writer.begin()
		for i in range(0, 10):
			buffer = SerializerHelper.Encode(
				str(i),
				format='text/plain',
				charset='utf-8'
			)
			writer.chunk(buffer)
			sleep(1)
		writer.chunk()
		writer.end()
		return
