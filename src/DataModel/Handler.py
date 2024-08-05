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
		model : any,  				# Model
		attr : any,						# Name
		value : any,  				# Value
		previousValue : any,	# Previous Value
	):
		pass