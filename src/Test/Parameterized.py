# -*- coding: utf-8 -*-

__all__ = (
	'Parameterized'
)


class Parameterized:
	"""Parameterized Decorator"""
	def __init__(self, *args) -> None:
		self.args = args
		return

	def __call__(self, fn):
		def method(this):
			for	arg in self.args:
				if isinstance(arg, (list, tuple)):
					fn(this, *arg)	
					continue
				if isinstance(arg, dict):
					fn(this, **arg)
					continue
		return method
