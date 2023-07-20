# -*- coding: utf-8 -*-

from .RequestRunner import RequestRunner
from .RequestFilter import RequestFilter
from .ResponseFilter import ResponseFilter
from .CrossOriginResourceSharing import CrossOriginResourceSharing

from .Validator import Validator

__all__ = (
	'RequestRunnerProperties',
)


class RequestRunnerProperties(object):
	"""
	Request Runner Properties Class
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
		onResponse : ResponseFilter = None,
		cors: CrossOriginResourceSharing = None,
	):
		self.__props__ = {
			'object': object,
			'method': method,
			'url': url,
			'qs': qs,
			'body': body,
			'onRequest': onRequest,
			'onRequestOrigin': onRequestOrigin,
			'onResponseOrigin': onResponseOrigin,
			'onResponse': onResponse,
			'cors': cors
		}
		return

	def __repr__(self):
		return repr(self.__props__)

	def __getitem__(self, key):
		return self.__props__.__getitem__(key)

	def __setitem__(self, key, value):
		self.__props__.__setitem__(key, value)

	def __delitem__(self, key):
		self.__props__.__delitem__(key)
		return

	def __len__(self):
		return len(self.__props__)

	def __iter__(self):
		return iter(self.__props__)

	def __contains__(self, key):
		return key in self.__props__

	def __copy__(self):
		return dict(self.__props__)

	def __deepcopy__(self, memo):
		return dict(self.__props__)

	def keys(self):
		return self.__props__.keys()

	def items(self):
		return self.__props__.items()
