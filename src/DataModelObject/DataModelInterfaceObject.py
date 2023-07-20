# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'DataModelInterfaceObject'
)


class DataModelInterfaceObject(ABC):
	@abstractmethod
	def __call__(
		self, 
		o : any,  # Model
		n : str,  # Name
		v : any,  # Value
	):
		pass