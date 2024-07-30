# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Handler'
)


class Handler(metaclass=ABCMeta):
	"""Handler Interface for Data Model"""

	@abstractmethod
	def __call__(
		self, 
		o : any,  # Model
		n : str,  # Name
		v : any,  # Value
		p : any,  # Previous Value
	):
		pass