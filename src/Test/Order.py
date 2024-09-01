# -*- coding: utf-8 -*-

from ..Template import Singleton

__all__ = (
	'Order'
)


class OrderContext(Singleton):
	def __init__(self) -> None:
		self.context = {}
		return
	def add(self, o, m, order):
		if o not in self.context:
			self.context[o] = {}
		self.context[o][m] = order
		return
	def get(self, o):
		if o not in self.context:
			return
		return self.context[o]
	

class Order:
	"""Order Decorator"""
	def __init__(self, order) -> None:
		self.order = order
		self.context = OrderContext()
		return

	def __call__(self, fn):
		o, *args = fn.__qualname__.split('.', 1)
		self.context.add(o, fn.__name__, self.order)
		return fn 

