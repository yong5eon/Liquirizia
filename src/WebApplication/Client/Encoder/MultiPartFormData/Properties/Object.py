# -*- coding: utf-8 -*-

__all__ = (
	'Object'
)


class Object(object):
	def headers(self):
		raise NotImplementedError('{} must be implemented headers'.format(self.__class__.__name__))

	def body(self):
		raise NotImplementedError('{} must be implemented body'.format(self.__class__.__name__))
