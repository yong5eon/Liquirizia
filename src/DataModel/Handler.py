# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from typing import Any

__all__ = (
	'Handler'
)


class Handler(metaclass=ABCMeta):
	"""Handler Interface for Data Model"""
	@abstractmethod
	def __call__(
		self,
		m, # model
		o, # value descriptor
		v: Any, # changed value
		p: Any,  # previous value
	):
		pass
