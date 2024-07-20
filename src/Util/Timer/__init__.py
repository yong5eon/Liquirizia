# -*- coding: utf-8 -*-

from .Timer import Timer
from .DurationTimer import DurationTimer
from .Decorator import Decorator

from functools import wraps

__all__ = (
	'DurationTimer',
	'Timer',
	'Duration',
)


def Duration(name: str = None, callback: callable = None):
	def decorator(fn):
		wraps(fn)
		return Decorator(fn, name, callback)
	return decorator
