# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import (
	Request,
	RequestReader,
	ResponseWriter,
)

__all__ = (
	'Runnable'
)


class Runnable(object):
	"""
	Runnable Abstract Class
	"""
	def run(self, request: Request, reader: RequestReader, writer: ResponseWriter, parameters: dict, version: str, server: str = None):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
