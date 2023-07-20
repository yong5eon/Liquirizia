# -*- coding: utf-8 -*-

__all__ = (
	'Handler'
)


class Handler(object):
	"""
	Runnable Handler Interface for Parallelize
	"""
	def onInitialize(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented onInitialize'.format(self.__class__.__name__))

	def onStart(self):
		raise NotImplementedError('{} must be implemented onStart'.format(self.__class__.__name__))

	def onCompleted(self):
		raise NotImplementedError('{} must be implemented onCompleted'.format(self.__class__.__name__))

	def onStopped(self):
		raise NotImplementedError('{} must be implemented onStopped'.format(self.__class__.__name__))

	def onError(self, error=None):
		raise NotImplementedError('{} must be implemented onError'.format(self.__class__.__name__))
