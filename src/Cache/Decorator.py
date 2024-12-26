# -*- coding: utf-8 -*-

from .Helper import Helper

from typing import Callable
from functools import wraps

from hashlib import sha256

__all__ = (
	'Decorator'
)


class Decorator(object):
	"""Decorator to apply cache in method of class and function"""
	def __init__(
		self,
		key: str,
		expires: int = None,
	):
		self.key = key
		self.expires = expires
		return

	def __call__(self, fn: Callable):
		def wrapper(*args, **kwargs):
			context = Helper.Get(self.key)
			if context:
				key = (fn.__qualname__, args, kwargs)
				v = context.get(key)
				if v is not None:
					return v
			v = fn(*args, **kwargs)
			if context:
				key = (fn.__qualname__, args, kwargs)
				context.set(key, v, expires=self.expires)
			return v
		return wrapper
