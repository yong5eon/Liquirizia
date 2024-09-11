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
		model,     # Model
		obj,       # Instance of Model
		attr,      # Attribute of Model
		value,     # Changed Value
		preValue,  # Previous Value
	):
		pass