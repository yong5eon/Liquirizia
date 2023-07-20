# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import RequestStreamRunner, Request, RequestReader, ResponseWriter

from time import sleep

__all__ = (
	'RunStreamOut'
)


class RunStreamOut(RequestStreamRunner):
	def __init__(self, request: Request, parameters):
		self.request = request
		self.parameters = parameters
		return

	def run(self, reader: RequestReader, writer: ResponseWriter):
		writer.status(200, 'OK')
		writer.header('Content-Type', 'text/plain; charset=utf-8')
		writer.header('Content-Length', str(10))
		writer.begin()
		for i in range(0, 10):
			writer.write(str(i).encode('utf-8'))
			sleep(1)
		writer.end()
		return
