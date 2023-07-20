# -*- coding: utf-8 -*-


from Liquirizia.WebApplication import (
	Request,
	RequestRunner,
	RequestFilter,
	ResponseFilter,
	RequestReader,
	ResponseWriter,
	CrossOriginResourceSharing,
)
from Liquirizia.WebApplication.Validator import Validator
from Liquirizia.WebApplication.Serializer import SerializerHelper

from ..Route import Route
from ..Runnable import Runnable

__all__ = (
	'Request'
)


class Run(Route, Runnable):
	"""
	Runner Class to serve web application
	"""

	def __init__(
		self,
		object: type(RequestRunner),
		method: str,
		url: str,
		qs: Validator = None,
		body: Validator = None,
		onRequest: RequestFilter = None,
		onRequestOrigin: RequestFilter = None,
		onResponseOrigin: ResponseFilter = None,
		onResponse: ResponseFilter = None,
		cors=CrossOriginResourceSharing(),
	):
		super(Run, self).__init__(method, url, cors=cors)
		self.object = object
		self.onRequest = onRequest
		self.onRequestOrigin = onRequestOrigin
		self.onResponseOrigin = onResponseOrigin
		self.onResponse = onResponse
		self.qs = qs
		self.body = body
		return

	def run(
		self,
		request: Request,
		reader: RequestReader,
		writer: ResponseWriter,
		parameters: dict,
		version: str,
		server: str = None
	):
		if request.size:
			request.body = SerializerHelper.Decode(
				reader.read(request.size),
				format=request.format,
				charset=request.charset,
			)

		if self.onRequest:
			request, response = self.onRequest.run(request)
			if response:
				writer.send(response, headers=self.headers(request))
				return response

		# TODO : do cache instead of origin
		if self.onRequestOrigin:
			request, response = self.onRequestOrigin.run(request)
			if response:
				writer.send(response, headers=self.headers(request))
				return response

		if self.qs:
			request.qs, response = self.qs(request.qs)
			if response:
				writer.send(response, headers=self.headers(request))
				return response

		if self.body:
			request.body, response = self.body(request.body)
			if response:
				writer.send(response, headers=self.headers(request))
				return response

		obj = self.object(request, parameters)
		response = obj.run(request.body)

		if self.onResponseOrigin:
			response = self.onResponseOrigin.run(response)

		if self.onResponse:
			response = self.onResponse.run(response)

		writer.send(response, headers=self.headers(request))
		return response
