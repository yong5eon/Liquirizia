# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import RequestRunner, Request
from Liquirizia.WebApplication.Responses import *

__all__ = (
	'RunGet'
)


class RunGet(RequestRunner):
	def __init__(self, request: Request, parameters):
		self.request = request
		self.parameters = parameters
		return

	def run(self, body=None):
		return ResponseJSON({
			'parameters': self.parameters,
			'a': self.request.qs['a'],
			'b': self.request.qs['b'],
			'c': self.request.qs['c']
		})
