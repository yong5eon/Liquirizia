# -*- coding: utf-8 -*-

from .Validator import Validator
from .Patterns import IsDictionary

from functools import wraps
from inspect import getfullargspec

__all__ = (
	'Validate',
)


class Validate(object):
	"""Decorator for Validator of Function and Method"""
	def __init__(self, mappings: dict):
		self.mappings = mappings
		return

	def __call__(self, fn: callable):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			validator = Validator(IsDictionary(self.mappings))
			kwargs = validator(self.__parameters__(fn, args, kwargs))
			return fn(**kwargs)
		return wrapper

	def __parameters__(self, fn, args, kwargs):
		# get description of function params expected
		spec = getfullargspec(fn)
		defs = dict(zip(spec.args[-len(spec.defaults):], spec.defaults))
		for arg in spec.args if isinstance(spec.args, (list, tuple,)) else []:
			if arg not in kwargs.keys():
				kwargs[arg] = defs[arg] if arg in defs.keys() else None
		for i, arg in enumerate(args) if isinstance(args, (list, tuple,)) else []:
			kwargs[spec.args[i]] = args[i]
		return kwargs
