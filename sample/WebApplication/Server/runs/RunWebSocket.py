# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import RequestWebSocketRunner, Request, WebSocket

__all__ = (
	'RunWebSocket'
)


class RunWebSocket(RequestWebSocketRunner):
	def __init__(self, request: Request, parameters):
		self.request = request
		self.parameters = parameters
		return

	def run(self, ws: WebSocket, op, buffer):
		if op == ws.OPCODE_PING:
			ws.pong(buffer)
		if op == ws.OPCODE_PONG:
			ws.ping(buffer)
		if op == ws.OPCODE_TEXT:
			ws.write(buffer, ws.OPCODE_TEXT)
		if op == ws.OPCODE_BINARY:
			ws.write(buffer, ws.OPCODE_BINARY)
		return
