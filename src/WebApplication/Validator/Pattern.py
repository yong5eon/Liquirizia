# -*- coding: utf-8 -*-

from Liquirizia.Validator import Pattern as Base

from ..Response import Response

__all__ = (
	'Pattern'
)


class Pattern(Base):
	"""
	Pattern Interface Class for Validator of Web Application
	"""
	def __call__(self, parameter) -> (any, (Response, None)):
		raise NotImplementedError('{} must be implemented __call__ and if condition is true, must return parameter'.format(self.__class__.__name__))
