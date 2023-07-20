# -*- coding: utf-8 -*-

__all__ = (
	'ServerHandler'
)


class ServerHandler(object):
	"""
	Web Application Server Handler Interface
	"""
	def onStart(self, host, port, version, name=None):
		raise NotImplementedError('{} must be implemented onStart'.format(self.__class__.__name__))

	def onConnected(self, address, port):
		raise NotImplementedError('{} must be implemented onConnected'.format(self.__class__.__name__))

	def onRequest(self, request):
		raise NotImplementedError('{} must be implemented onRequest'.format(self.__class__.__name__))

	def onRequestSuccess(self, request, response=None):
		raise NotImplementedError('{} must be implemented onRequestSuccess'.format(self.__class__.__name__))

	def onRequestError(self, request, e):
		raise NotImplementedError('{} must be implemented onRequestError'.format(self.__class__.__name__))

	def onClosed(self, address, port):
		raise NotImplementedError('{} must be implemented onClosed'.format(self.__class__.__name__))

	def onError(self, e):
		raise NotImplementedError('{} must be implemented onError'.format(self.__class__.__name__))

	def onStop(self):
		raise NotImplementedError('{} must be implemented onStop'.format(self.__class__.__name__))
