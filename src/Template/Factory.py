# -*- coding: utf-8 -*-

from abc import ABCMeta
from sys import _getframe as getframe
from inspect import (
	getmodule,
	getfullargspec,
	getcallargs,
	getmembers,
	isfunction,
	ismethod,
)

__all__ = (
	'Factory'
)


class Factory(object):
	"""
	Factory Design Pattern Base Class

	class YourObject(Factory):
		
		def onCreate(self, *args, **kwargs):
			pass

		pass

	a=YOurObject(...)  # fail
	b=YourObject.CreateInstance(...)  # success
	"""
	@classmethod
	def __new__(Object, *args, **kwargs):
		caller = getframe(1)
		code = caller.f_code
		name = code.co_name
		if not name == 'CreateInstance':
			raise RuntimeError('You have to use CreateInstance instead of constructor to create instance')
		obj = object.__new__(Object)
		return obj

	@classmethod
	def CreateInstance(Object, *args, **kwargs):
		raise NotImplementedError('You have to define CreateInstance to create instance')

