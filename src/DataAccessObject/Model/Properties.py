# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Properties',
)


class Properties(metaclass=ABCMeta):
	"""Interface to Declare Properties of Model as a Decorator"""
	@abstractmethod
	def __call__(self, obj):
		pass