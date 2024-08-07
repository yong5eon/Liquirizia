# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'ModelHandler'
)


class ModelHandler(ABC):
	@abstractmethod
	def __call__(
		self, 
		o : any,  # Model
		n : str,  # Name
		v : any,  # Value
		p : any,  # Previous Value
	):
		pass